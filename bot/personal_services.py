"""Personal life management stubs for the Telegram bot."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List
import datetime as dt


@dataclass
class Task:
    description: str
    created_at: dt.datetime
    done: bool = False


@dataclass
class Habit:
    name: str
    last_checked: dt.date | None = None


class PersonalClient:
    def __init__(self) -> None:
        self.tasks: List[Task] = []
        self.habits: List[Habit] = []
        self.inbox: List[str] = ["Follow up on invoices", "Schedule dentist appointment"]

    def list_tasks(self) -> List[str]:
        if not self.tasks:
            return ["No tasks yet"]
        return [f"{'[x]' if task.done else '[ ]'} {task.description}" for task in self.tasks]

    def add_task(self, description: str) -> Task:
        task = Task(description=description, created_at=dt.datetime.utcnow())
        self.tasks.append(task)
        return task

    def list_habits(self) -> List[str]:
        return [f"{habit.name} (last check: {habit.last_checked or 'never'})" for habit in self.habits]

    def add_habit(self, name: str) -> Habit:
        habit = Habit(name=name)
        self.habits.append(habit)
        return habit

    def calendar_digest(self) -> List[str]:
        today = dt.date.today()
        return [
            f"{today} — Team standup",
            f"{today + dt.timedelta(days=1)} — Inventory audit",
        ]

    def add_note(self, topic: str) -> str:
        self.inbox.append(f"Note captured: {topic}")
        return topic

    def inbox_summary(self) -> List[str]:
        return list(self.inbox)
