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
