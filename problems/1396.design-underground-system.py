#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#

# @lc code=start
class UndergroundSystem:

    def __init__(self):
        self.travel_times = {}

        self.checkins = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, check_in_time = self.checkins[id]
        travel = (startStation, stationName)
        travel_time = t - check_in_time

        if travel in self.travel_times:
            total_time, count = self.travel_times[travel]
            self.travel_times[travel] = (total_time + travel_time, count + 1)
        else:
            self.travel_times[travel] = (travel_time, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel = (startStation, endStation)
        total_time, count = self.travel_times[travel]
        return total_time / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end

