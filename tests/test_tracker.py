from src.core.tracker import TimeTracker

def main():
    tracker = TimeTracker(check_interval=10)
    tracker.start()

if __name__ == "__main__":
    main()



