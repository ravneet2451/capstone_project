"""Planner Agent
Generates a simple study plan from syllabus, exam date and available hours.
This is intentionally straightforward; extend with smarter heuristics.
"""
from datetime import datetime, timedelta
import math




class PlannerAgent:
def __init__(self, memory_agent=None):
self.memory = memory_agent


def create_study_plan(self, syllabus, exam_date, available_hours):
"""
syllabus: list of {"topic": str, "estimate_hours": int}
exam_date: string 'YYYY-MM-DD'
available_hours: list of daily available hours or int
"""
# parse exam date
exam = datetime.fromisoformat(exam_date)
today = datetime.now()
days_left = max((exam - today).days, 1)


# flatten available hours
if isinstance(available_hours, int):
hours_per_day = available_hours
elif isinstance(available_hours, list):
hours_per_day = sum(available_hours) / len(available_hours)
else:
hours_per_day = 2


total_available = days_left * hours_per_day
total_required = sum(item.get("estimate_hours", 1) for item in syllabus)


factor = max(1, total_required / total_available)


# allocate topics across days
plan = {str((today + timedelta(days=i)).date()): [] for i in range(days_left)}


day_indices = list(plan.keys())
di = 0
for topic in syllabus:
needed = max(1, math.ceil(topic.get("estimate_hours", 1) / hours_per_day * factor))
for _ in range(needed):
day = day_indices[di % len(day_indices)]
plan[day].append(topic["topic"])
di += 1


return {"exam_date": exam_date, "days_left": days_left, "plan": plan}
