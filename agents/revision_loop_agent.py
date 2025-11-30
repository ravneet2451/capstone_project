"""Revision Loop Agent
Uses memory to recommend topics for revision.
"""




class RevisionLoopAgent:
def __init__(self, memory_agent):
self.memory = memory_agent


def recommend_revision(self, num_topics=3):
weak = self.memory.get_weak_topics()
# if no weak topics, recommend high-level topics
if not weak:
return ["scheduled review", "practice questions", "self-assessment"]


# return top N weak topics
return weak[:num_topics]
