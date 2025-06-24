import json
from datetime import datetime
from typing import List, Dict

class PersistenceError(Exception):
    """Raised when saving/loading habits fails."""
    pass

class Habit:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__history: List[str] = []

    def mark_done(self, date: str) -> None:
        if date not in self.__history:
            self.__history.append(date)
            self.__history.sort()

    def streak(self) -> int:
        from datetime import timedelta
        today = datetime.today()
        dates = [datetime.strptime(d, "%Y-%m-%d") for d in self.__history]
        dates.sort(reverse=True)

        streak = 0
        for i, d in enumerate(dates):
            if i == 0:
                if (today - d).days > 1:
                    break
                streak += 1
            else:
                if (dates[i - 1] - d).days == 1:
                    streak += 1
                else:
                    break
        return streak

    def __str__(self) -> str:
        return f"{self.name}: {self.description} ({len(self.__history)} days done)"

    def __repr__(self) -> str:
        return f"Habit(name={self.name!r}, description={self.description!r})"

    def to_dict(self) -> Dict:
        return {"name": self.name, "description": self.description, "history": self.__history}

    @classmethod
    def from_dict(cls, data: Dict):
        h = cls(data["name"], data["description"])
        h.__history = data["history"]
        return h


class HabitTracker:
    DATE_FORMAT = "%Y-%m-%d"

    def __init__(self):
        self.habits: Dict[str, Habit] = {}

    def add_habit(self, name: str, desc: str) -> None:
        self.habits[name] = Habit(name, desc)

    def remove_habit(self, name: str) -> None:
        if name in self.habits:
            del self.habits[name]

    def mark_done(self, name: str, date: str = None) -> None:
        if name in self.habits:
            if not date:
                date = datetime.today().strftime(self.DATE_FORMAT)
            self.habits[name].mark_done(date)

    def list_habits(self) -> List[Habit]:
        return list(self.habits.values())

    def report(self) -> Dict[str, int]:
        return {name: habit.streak() for name, habit in self.habits.items()}

    def save(self, filename: str) -> None:
        try:
            with open(filename, "w") as f:
                json.dump({name: h.to_dict() for name, h in self.habits.items()}, f, indent=2)
        except OSError as e:
            raise PersistenceError("Error saving file") from e

    def load(self, filename: str) -> None:
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.habits = {name: Habit.from_dict(h) for name, h in data.items()}
        except FileNotFoundError:
            self.habits = {}
        except json.JSONDecodeError as e:
            raise PersistenceError("Error loading file") from e

    def __add__(self, other):
        merged = HabitTracker()
        merged.habits = {**self.habits}
        for name, habit in other.habits.items():
            if name in merged.habits:
                merged.habits[name]._Habit__history = list(set(
                    merged.habits[name]._Habit__history + habit._Habit__history
                ))
            else:
                merged.habits[name] = habit
        return merged


def summarize(obj):
    print(f"{obj.name} — Streak: {obj.streak()} days")
