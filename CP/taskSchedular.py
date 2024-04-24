class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = Counter(tasks)
        maxFrequency = max(taskCount.values())
        maxTask = list(taskCount.values()).count(maxFrequency)
        intervalsNeeded = (maxFrequency-1) * (n+1) + maxTask
        return max(intervalsNeeded,len(tasks))