🧠 CLI Habit Tracker
A simple Command-Line Habit Tracker built with Python, integrating core concepts like object-oriented programming, data structures, file I/O, exception handling, and CLI interaction. Track your daily habits, mark them as done, review streaks, and save progress between runs.

📁 Project Structure


├── habits.py        
├── cli.py             
├── habits.json       
└── README.md        


Run the CLI
python cli.py

Menu Options
1. Add new habit
2. Remove habit
3. Mark habit done
4. List all habits
5. Show streak report
6. Save & Exit

🧩 Key Features
Feature	Description
✅ Add/Remove Habit	Easily manage your habits
📅 Mark Done	Track progress with dates (auto or manual entry)
🔁 Streak Report	View your current streak for each habit
💾 Persistence	Save and load habit data using JSON
🔧 Error Handling	Robust handling for file errors, invalid inputs
➕ Merge Support	Combine two HabitTracker instances using + operator
🦆 Duck Typing Tool	summarize(obj) prints habit name and streak dynamically


🧠 Learning Objectives (Concept Mapping)
Day	Concept	Application in Project
1	Python Basics & Functions	Habit methods, CLI logic
2	OOP (Classes, Objects)	Habit and HabitTracker classes
3	File I/O & Exceptions	JSON persistence & PersistenceError
4	Data Structures	Lists (history), Dicts (habit storage)
5	CLI and Utility Functions	summarize, menu handling, input validation

🛠 Bonus Tools
✅ Operator Overloading (+) for merging two HabitTracker instances.

⏱️ Optional timer context manager available in habits.py to benchmark functions.

📌 Notes
All dates must follow YYYY-MM-DD format.

Use with open(...) for all file operations.

If habits.json is not found, a new tracker is initialized.










