import sys
import argparse
from src.core.tracker import TimeTracker
from src.storage.json_storage import JsonStorage

def main():
    parser = argparse.ArgumentParser(
        description="DevTimeTracker - smart time tracker for developers",
        epilog="Examples:\n devtime start\n devtime stats\n devtime stop"
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands")

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

    else:
        parser.print_help()

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

    print("\n📊 STATISTICS FOR ALL TIME")
    print("=" * 40)
    total = sum(total_editor_stats.values())
    hours = total // 3600
    minutes = (total % 3600) // 60

    print(f"Total time: {hours}h {minutes}m")
    print("\nBy editor:")
    for editor, seconds in sorted(total_editor_stats.items(),
                                  key=lambda x: x[1], reverse=True):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        print(f" {editor}: {h}h {m}m")

    print(f"\n📅 LAST {days} DAYS")
    print("=" * 40)

    sorted_dates = sorted(daily_stats.keys(), reverse=True)[:days]
    for date in sorted_dates:
        editors = daily_stats[date]
        total_day = sum(editors.values())
        h = total_day // 3600
        m = (total_day % 3600) // 60
        print(f"{date}: {h}h {m}m")
        for editor, seconds in editors.items():
            sh = seconds // 3600
            sm = (seconds % 3600) // 60
            print(f" {editor}: {sh}h {sm}m")



