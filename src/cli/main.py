import sys
import argparse
import subprocess
import platform
from datetime import datetime

from src.core.tracker import TimeTracker
from src.storage.json_storage import JsonStorage
from src.daemon.autostart import enable, disable, is_enabled


def main():
    parser = argparse.ArgumentParser(
        description="DevTimeTracker - smart time tracker for developers",
        epilog="Examples:\n devtime start\n devtime stats\n devtime stop"
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands")

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

    else:
        parser.print_help()

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


def _show_stats(storage: JsonStorage, days: int):
    all_data = storage.load_all()
    daily_stats = all_data.get('daily_stats', {})

    if not daily_stats:
        print("📊 No data yet. Tracker hasn't been used.")
        return

    total_editor_stats = {}
    for date, editors in daily_stats.items():
        for editor, seconds in editors.items():
            if editor not in total_editor_stats:
                total_editor_stats[editor] = 0
            total_editor_stats[editor] += seconds

    total_seconds = sum(total_editor_stats.values())
    total_hours = total_seconds // 3600
    total_minutes = (total_seconds % 3600) // 60

    days_count = len(daily_stats)
    avg_seconds = total_seconds // days_count if days_count > 0 else 0
    avg_hours = avg_seconds // 3600
    avg_minutes = (avg_seconds % 3600) // 60

    print("\n📊 STATISTICS FOR ALL TIME")
    print("=" * 40)
    print(f"Total time:       {total_hours}h {total_minutes}m")
    print(f"Days tracked:     {days_count}")
    print(f"Average/day:      {avg_hours}h {avg_minutes}m")

    streak = _calculate_streak(daily_stats)
    if streak > 0:
        print(f"🔥 Streak: {streak} days in a row!")

    print("\n🖥️ BY EDITOR:")
    for editor, seconds in sorted(total_editor_stats.items(),
                                  key=lambda x: x[1], reverse=True):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        print(f" {editor}: {h}h {m}m")

    print(f"\n📅 LAST {days} DAYS")
    print("=" * 40)

    sorted_dates = sorted(daily_stats.keys(), reverse=True)[:days]

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
        print(f"{date}: {h}h {m}m")

        bar = _make_bar(total_day, max_day_seconds)
        print(f"{date}: {bar} {h}h {m}m")


def _show_status():
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


if __name__ == "__main__":
    main()


