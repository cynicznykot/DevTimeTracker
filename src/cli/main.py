"""
DevTimeTracker CLI entry point.

This module provides the command-line interface for DevTimeTracker.
It handles argument parsing and dispatches commands to the appropriate
modules.

Commands:
    start       Start tracking time
    stop        Stop tracking (instructions)
    status      Show tracker status
    stats       Show statistics
    export      Export statistics to CSV/JSON
    autostart   Manage autostart
    tray        Run system tray icon

Example:
    $ devtime start
    $ devtime stats -d 30
    $ devtime export --format csv
"""


import sys
import argparse
import subprocess
import platform
from datetime import datetime
from typing import Optional

from src.core.tracker import TimeTracker
from src.storage.json_storage import JsonStorage
from src.daemon.autostart import enable, disable, is_enabled


# =======================================================================================
# CLI PARSER
# =======================================================================================

def _create_parses() -> argparse.ArgumentParser:
    """
    Create and configure the argument parses.

    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        description="DevTimeTracker - smart time tracker for developers",
        epilog="Examples:\n"
        " devtime start\n"
        " devtime stats -d 30\n"
        " devtime export --format csv\n"
        " devtime autostart enable"
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # --- Start ---
    start_parser = subparsers.add_parser("start", hepl="Start tracking")
    start_parser.add_argument(
        "-i", "--interval",
        type=int,
        default=10,
        help="Check interval in seconds (default: 10)"
    )

    # --- Stop ---
    subparsers.add_parser("stop", help="Stop tracking")

    # --- Status ---
    subparsers.add_parser("stop", help="Show tracker status")

    # --- Stats ---
    stats_parser = subparsers.add_parser("stats", help="Show statistics")
    stats_parser.add_argument(
        "-d", "--days",
        type=int,
        default=7,
        help="Statistics for last N days (default: 7)"
    )

    # --- Export ---
    export_parser = subparsers.add_parser("export", help="Export statistics")
    export_parser.add_argument(
        "--format",
        choices=["csv", "json"],
        default="csv",
        help="Export format (default: csv)"
    )
    export_parser.add_argument(
        "-o", "--output",
        type=int,
        default=None,
        help="Output file path"
    )

    # --- Autostart ---
    autostart_parses = subparsers.add_parser("autostart", help="Manage autostart")
    autostart_subparsers = autostart_parses.add_subparsers(dest="autostart_action")

    autostart_subparsers.add_parser("enable", help="Enable autostart")
    autostart_subparsers.add_parser("disable", help="Disable autostart")
    autostart_subparsers.add_parser("status", help="Check autostart status")

    # --- Tray ---
    subparsers.add_parser("tray", help="Run system tray icon")

    return parser


# =======================================================================================
# HELPER FUNCTIONS
# =======================================================================================

def _format_duration(seconds: int) -> str:
    """
    Format duration in seconds to a human-readable string.

    Args:
        seconds: Duration in seconds.

    Returns:
        Formatted string like "2h 30m" or "45s".

    Examples:
        >>> _format_duration(9000)
        '2h 30m'
        >>> _format_duration(45)
        '45s'
    """
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    if hours > 0:
        return f"{hours}h {minutes}m"
    elif minutes > 0:
        return f"{minutes}m {secs}s"
    else:
        return f"{secs}s"


def _make_bar(seconds: int, max_seconds: int, width: int = 20) -> str:
    """
    Create a text bar for visualization.

    Args:
        seconds: Time in seconds.
        max_seconds: Maximum time for scaling.
        width: Width of the bar in characters.

    Returns:
        String with bar characters.
    """
    if max_seconds == 0:
        return ""

    filled = int(seconds / max_seconds * width)
    return "█" * filled


def _calculate_streak(daily_stats: dict) -> int:
    """
    Calculate the current streak of consecutive days.

    Args:
        daily_stats: Dictionary of daily statistics.

    Returns:
        Number of consecutive days with activity.
    """
    if not daily_stats:
        return 0

    sorted_dates = sorted(daily_stats.keys(), reverse=True)

    streak = 1
    today = datetime.now().date()
    first_date = datetime.strptime(sorted_dates[0], "%Y-%m-%d").date()

    if (today - first_date).days > 1:
        return 0

    for i in range(1, len(sorted_dates)):
        current = datetime.strptime(sorted_dates[i - 1], "%Y-%m-%d").date()
        prev = datetime.strptime(sorted_dates[i], "%Y-%m-%d").date()

        if (current - prev).days == 1:
            streak += 1
        else:
            break

    return streak


def _print_editor_stats(editor_stats: dict, total_seconds: int) -> None:
    """
    Print statistics grouped by editor.

    Args:
        editor_stats: Dictionary mapping editor name to seconds.
        total_seconds: Total time in seconds (for percentages).
    """
    if not editor_stats:
        return

    print("\n🖥️ BY EDITOR:")
    max_seconds = max(editor_stats.values())
    max_name_len = max(len(name) for name in editor_stats.keys())

    for editor, seconds in sorted(editor_stats.items(), key=lambda x: x[1], reverse=True):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        percent = (seconds / total_seconds * 100) if total_seconds > 0 else 0
        bar = _make_bar(seconds, max_seconds, width=15)
        name_padded = editor.ljust(max_name_len)
        print(f"  {name_padded}: {bar} {h}h {m}m ({percent:.0f}%)")


def _print_language_stats(language_stats: dict, total_seconds: int) -> None:
    """
    Print statistics grouped by language.

    Args:
        language_stats: Dictionary mapping language name to seconds.
        total_seconds: Total time in seconds (for percentage).
    """
    if not language_stats:
        return

    print(f"\n📝 BY LANGUAGE:")
    max_seconds = max(language_stats.values())
    max_name_len = max(len(name) for name in language_stats.keys())

    for language, seconds in sorted(language_stats.items(), key=lambda x: x[1], reverse=True):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        percent = (seconds / total_seconds * 100) if total_seconds > 0 else 0
        bar = _make_bar(seconds, max_seconds, width=15)
        name_padded = language.ljust(max_name_len)
        print(f"  {name_padded}: {bar} {h}h {m}m ({percent:.0f}%)")


def _print_daily_stats(daily_stats: dict, days: int) -> None:
    """
    Print statistics for the last N days.

    Args:
        daily_stats: Dictionary of daily statistics.
        days: Number of days to show.
    """
    print(f"\n📅 LAST {days} DAYS")
    print("=" * 40)

    sorted_dates = sorted(daily_stats.keys(), reverse=True)[:days]

    # Find max for scaling
    max_day_seconds = 0
    for date in sorted_dates:
        total_day = sum(daily_stats[date].values())
        if total_day > max_day_seconds:
            max_day_seconds = total_day

    for date in sorted_dates:
        editors = daily_stats[date]
        total_day = sum(editors.values())
        h = total_day // 3600
        m = (total_day % 3600) // 60
        bar = _make_bar(total_day, max_day_seconds)
        print(f"{date}: {bar} {h}h {m}m")


# =======================================================================================
# COMMAND HANDLERS
# =======================================================================================

def _show_stats(storage: JsonStorage, days: int) -> None:
    """
    Show statistics for all time and last N days.

    Args:
        storage: JsonStorage instance.
        days: Number of days to show.
    """
    all_data = storage.load_all()
    daily_stats = all_data.get('daily_stats', {})

    if not daily_stats:
        print("📊 No data yet. Tracker hasn't been used.")
        return

    # Aggregate editor stats
    total_editor_stats = {}
    for date, editors in daily_stats.items():
        for editor, seconds in editors.items():
            total_editor_stats[editor] = total_editor_stats.get(editor, 0) + seconds

    total_seconds = sum(total_editor_stats.values())
    days_count = len(daily_stats)
    avg_seconds = total_seconds // days_count if days_count > 0 else 0

    # === Header ===
    print("\n📊 STATISTICS FOR ALL TIME")
    print("=" * 40)
    print(f"Total time:       {_format_duration(total_seconds)}")
    print(f"Days tracked:     {days_count}")
    print(f"Average/day:      {_format_duration(avg_seconds)}")

    # === Streak ===
    streak = _calculate_streak(daily_stats)
    if streak > 0:
        print(f"🔥 Streak: {streak} days in a row!")

    # === By editor ===
    _print_editor_stats(total_editor_stats, total_seconds)

    # === By language ===
    language_stats = storage.get_language_stats()
    _print_daily_stats(language_stats, total_seconds)

    # === Last N days ===
    _print_daily_stats(daily_stats, days)


def _show_status() -> None:
    """
    Show tracker status (running or not).

    Uses platform-specific commands:
    - Windows: tasklist
    - Linux/macOS: pgrep
    """
    system = platform.system()

    if system == "Windows":
        result = subprocess.run(
            ['tasklist', '/FI', 'IMAGENAME eq python.exe', '/FO', 'CSV'],
            capture_output=True,
            text=True
        )

        if 'python.exe' in result.stdout and 'src.cli.main' in result.stdout:
            print("✅ Tracker is running")
        else:
            print("❌ Tracker is not running")
            print("    Start with: python -m src.cli.main start")

    else:
        # Linux/macOS: use pgrep
        result = subprocess.run(['pgrep', '-f', 'tracker'], capture_output=True)

        if result.returncode == 0:
            pids = result.stdout.decode().strip().split('\n')
            print("✅ Tracker is running")
            print(f"    PID: {', '.join(pids)}")
        else:
            print("❌ Tracker is not running")
            print("    Start with: devtime start")


# ======================================================================================
# COMMAND DISPATCHER
# ======================================================================================

def _handle_autostart(action: Optional[str], parser: argparse.ArgumentParser) -> None:
    """
    Handle autostart command.

    Args:
        action: Action to perform (enable/disable/status).
        parser: Autostart subparser (for help message).
    """
    if action == 'enable':
        if enable():
            print("✅ Autostart enabled")
        else:
            print("❌ Failed to enable autostart")

    elif action == 'disable':
        if disable():
            print("✅ Autostart disabled")
        else:
            print("⚠️ Autostart was not enabled")

    elif action == 'status':
        if is_enabled():
            print("✅ Autostart is enabled")
        else:
            print("❌ Autostart is disabled")

    else:
        parser.print_help()


def _handle_export(fmt: str, output: Optional[str]) -> None:
    """
    Handle export command.

    Args:
        fmt: Export format (csv/json).
        output: Output file path.
    """
    from src.storage.exporter import DataExporter

    storage = JsonStorage()
    exporter = DataExporter(storage)

    if fmt == 'csv':
        exporter.export_csv(output or "stats_export.csv")
    elif fmt == 'json':
        exporter.export_json(output or "stats_export.json")

        
def main():
    parser = argparse.ArgumentParser(
        description="DevTimeTracker - smart time tracker for developers",
        epilog="Examples:\n devtime start\n devtime stats\n devtime stop"
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Tray
    tray_parser = subparsers.add_parser('tray', help="Run system tray icon")

    # Autostart
    autostart_parser = subparsers.add_parser("autostart", help="Manage autostart")
    autostart_subparsers = autostart_parser.add_subparsers(dest="autostart_action")

    autostart_subparsers.add_parser("enable", help="Enable autostart")
    autostart_subparsers.add_parser("disable", help="Disable autostart")
    autostart_subparsers.add_parser("status", help="Check autostart status")

    # Start
    start_parser = subparsers.add_parser("start", help="Start Tracking")
    start_parser.add_argument("-i", "--interval", type=int, default=10,
                                help="Check interval in seconds (default: 10)")

    # Stats
    stats_parser = subparsers.add_parser("stats", help="Show statistics")
    stats_parser.add_argument("-d", "--days", type=int, default=7,
                                help="Statistic for last N day (default: 7)")

    # Stop
    stop_parser = subparsers.add_parser("stop", help="Stop Tracking")

    # Status
    status_parser = subparsers.add_parser("status", help="Show tracker status")

    # Export
    export_parser = subparsers.add_parser("export", help="Export statistics")
    export_parser.add_argument("--format", choices=["csv", "json", ], default="csv",
                               help="Export format (default: csv)")
    export_parser.add_argument("-o", "--output", type=str, default=None, help="Output file path")

    args = parser.parse_args()

    if args.command == "start":
        tracker = TimeTracker(check_interval=args.interval)
        tracker.start()

    elif args.command == "stats":
        storage = JsonStorage()
        _show_stats(storage, args.days)

    elif args.command == "stop":
        print("⏹️ Tracker stopping...")
        print("(use Ctrl+C in the terminal running the tracker)")
        print(" Or press: killall python3")

    elif args.command == "status":
        _show_status()

    elif args.command == "tray":
        from src.gui.tray import TrayIcon

        tracker = TimeTracker()
        tray = TrayIcon(tracker)
        tray.run()

    elif args.command == "autostart":
        if args.autostart_action == "enable":
            if enable():
                print("✅ Autostart enabled")
            else:
                print("❌ Failed to enable autostart")

        elif args.autostart_action == "disable":
            if disable():
                print("✅ Autostart disabled")
            else:
                print("⚠️ Autostart was not enabled")

        elif args.autostart_action == "status":
            if is_enabled():
                print("✅ Autostart is enabled")
            else:
                print("❌ Autostart is disabled")

        else:
            autostart_parser.print_help()

    elif args.command == "export":
        from src.storage.exporter import DataExporter

        storage = JsonStorage()
        exporter = DataExporter(storage)

        if args.format == "csv":
            output = args.output or "stats_export.csv"
            exporter.export_csv(output)
        elif args.format == "json":
            output = args.output or "stats_export.json"
            exporter.export_json(output)

    else:
        parser.print_help()



if __name__ == "__main__":
    main()


