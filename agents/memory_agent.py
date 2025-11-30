"""Memory Agent
Simple memory bank backed by a JSON file via SessionStore.
"""
from typing import List




class MemoryAgent:
def __init__(self, session_store):
self.store = session_store


def record_session(self, topic: str, success: bool, notes: str = ""):
rec = {"topic": topic, "success": success, "notes": notes}
self.store.append_record(rec)


def get_weak_topics(self) -> List[str]:
# define 'weak' as topics with repeated failures
records = self.store.get_records()
counts = {}
for r in records:
t = r.get("topic")
if not r.get("success"):
counts[t] = counts.get(t, 0) + 1
# sort by failures desc
sorted_topics = sorted(counts.items(), key=lambda x: x[1], reverse=True)
return [t for t, _ in sorted_topics]
