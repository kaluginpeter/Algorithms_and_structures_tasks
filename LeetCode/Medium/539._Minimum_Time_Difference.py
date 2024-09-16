# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
#
#
# Example 1:
#
# Input: timePoints = ["23:59","00:00"]
# Output: 1
# Example 2:
#
# Input: timePoints = ["00:00","23:59","00:00"]
# Output: 0
#
#
# Constraints:
#
# 2 <= timePoints.length <= 2 * 104
# timePoints[i] is in the format "HH:MM".
# Solution String Math
# Python O(NlogN) O(N) DateTime
from datetime import datetime, timedelta
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        answer: int = 23 * 60 * 60
        for idx in range(len(timePoints)):
            first_time = datetime.strptime(timePoints[idx], '%H:%M')
            second_time = datetime.strptime(timePoints[(idx + 1) % len(timePoints)], '%H:%M')
            if second_time < first_time:
                second_time += timedelta(days=1)
            answer = min(answer, (second_time - first_time).total_seconds() / 60)
        return int(answer)
# Python O(NlogN) O(1) Math
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for idx in range(len(timePoints)):
            hours, minutes = map(int, timePoints[idx].split(':'))
            timePoints[idx] = hours * 60 + minutes
        timePoints.sort()
        answer: int = 24 * 60 - timePoints[-1] + timePoints[0]
        for i in range(len(timePoints) - 1):
            answer = min(answer, timePoints[i + 1] - timePoints[i])
        return answer