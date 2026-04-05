"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        #print(sorted(intervals, key=lambda x: x[1]))

        tmp = []
        for i in intervals:
            tmp.append((i.start, i.end))

        new = sorted(tmp, key=lambda x: x[1])
        for i in range(1, len(new)):
            if new[i - 1][0] >= new[i][0] \
            or new[i - 1][1] >= new[i][1] \
            or new[i - 1][1] > new[i][0] \
            or new[i - 1][0] >= new[i][1]:
                return False
        return True

