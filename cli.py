from habits import HabitTracker, PersistenceError
from datetime import datetime

FILENAME = "habits.json"

def display_menu():
    print("\nHabit Tracker Menu")
    print("1. Add new habit")
    print("2. Remove habit")
    print("3. Mark habit done")
    print("4. List all habits")
    print("5. Show streak report")
    print("6. Save & Exit")

def main():
    tracker = HabitTracker()
    try:
        tracker.load(FILENAME)
        print("Habits loaded successfully.")
    except PersistenceError:
        print("Warning: Failed to load habits. Starting fresh.")

    while True:
        display_menu()
        try:
            choice = int(input("Choose an option (1-6): "))
        except ValueError:
            print("Invalid input. Enter a number from 1 to 6.")
            continue

        if choice == 1:
            name = input("Enter habit name: ")
            desc = input("Enter description: ")
            tracker.add_habit(name, desc)
        elif choice == 2:
            name = input("Enter habit name to remove: ")
            tracker.remove_habit(name)
        elif choice == 3:
            name = input("Enter habit name to mark done: ")
            date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
            if not date:
                tracker.mark_done(name)
            else:
                try:
                    datetime.strptime(date, "%Y-%m-%d")
                    tracker.mark_done(name, date)
                except ValueError:
                    print("Invalid date format.")
        elif choice == 4:
            habits = tracker.list_habits()
            if habits:
                for h in habits:
                    print(h)
            else:
                print("No habits found.")
        elif choice == 5:
            report = tracker.report()
            for name, streak in report.items():
                print(f"{name}: {streak} day streak")
        elif choice == 6:
            try:
                tracker.save(FILENAME)
                print("Habits saved. Exiting.")
            except PersistenceError:
                print("Failed to save habits.")
            break
        else:
            print("Choose between 1 and 6.")

if __name__ == "__main__":
    main()

