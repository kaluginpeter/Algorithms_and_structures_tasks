# Design a data structure that can efficiently manage data packets in a network router. Each data packet consists of the following attributes:
#
# source: A unique identifier for the machine that generated the packet.
# destination: A unique identifier for the target machine.
# timestamp: The time at which the packet arrived at the router.
# Implement the Router class:
#
# Router(int memoryLimit): Initializes the Router object with a fixed memory limit.
#
# memoryLimit is the maximum number of packets the router can store at any given time.
# If adding a new packet would exceed this limit, the oldest packet must be removed to free up space.
# bool addPacket(int source, int destination, int timestamp): Adds a packet with the given attributes to the router.
#
# A packet is considered a duplicate if another packet with the same source, destination, and timestamp already exists in the router.
# Return true if the packet is successfully added (i.e., it is not a duplicate); otherwise return false.
# int[] forwardPacket(): Forwards the next packet in FIFO (First In First Out) order.
#
# Remove the packet from storage.
# Return the packet as an array [source, destination, timestamp].
# If there are no packets to forward, return an empty array.
# int getCount(int destination, int startTime, int endTime):
#
# Returns the number of packets currently stored in the router (i.e., not yet forwarded) that have the specified destination and have timestamps in the inclusive range [startTime, endTime].
# Note that queries for addPacket will be made in increasing order of timestamp.
#
#
#
# Example 1:
#
# Input:
# ["Router", "addPacket", "addPacket", "addPacket", "addPacket", "addPacket", "forwardPacket", "addPacket", "getCount"]
# [[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]
#
# Output:
# [null, true, true, false, true, true, [2, 5, 90], true, 1]
#
# Explanation
#
# Router router = new Router(3); // Initialize Router with memoryLimit of 3.
# router.addPacket(1, 4, 90); // Packet is added. Return True.
# router.addPacket(2, 5, 90); // Packet is added. Return True.
# router.addPacket(1, 4, 90); // This is a duplicate packet. Return False.
# router.addPacket(3, 5, 95); // Packet is added. Return True
# router.addPacket(4, 5, 105); // Packet is added, [1, 4, 90] is removed as number of packets exceeds memoryLimit. Return True.
# router.forwardPacket(); // Return [2, 5, 90] and remove it from router.
# router.addPacket(5, 2, 110); // Packet is added. Return True.
# router.getCount(5, 100, 110); // The only packet with destination 5 and timestamp in the inclusive range [100, 110] is [4, 5, 105]. Return 1.
# Example 2:
#
# Input:
# ["Router", "addPacket", "forwardPacket", "forwardPacket"]
# [[2], [7, 4, 90], [], []]
#
# Output:
# [null, true, [7, 4, 90], []]
#
# Explanation
#
# Router router = new Router(2); // Initialize Router with memoryLimit of 2.
# router.addPacket(7, 4, 90); // Return True.
# router.forwardPacket(); // Return [7, 4, 90].
# router.forwardPacket(); // There are no packets left, return [].
#
#
# Constraints:
#
# 2 <= memoryLimit <= 105
# 1 <= source, destination <= 2 * 105
# 1 <= timestamp <= 109
# 1 <= startTime <= endTime <= 109
# At most 105 calls will be made to addPacket, forwardPacket, and getCount methods altogether.
# queries for addPacket will be made in increasing order of timestamp.
# Solution
# C++
# addPacket -> O(1)
# forwardPacket -> O(1)
# getCount -> O(logN)
# Memory Complexity O(N)
# DoubleEndedQueue HashMap HashSet BinarySearch
struct TupleHash {
    size_t operator()(const std::tuple<int, int, int>& t) const {
        auto hash1 = std::hash<int>{}(std::get<0>(t));
        auto hash2 = std::hash<int>{}(std::get<1>(t));
        auto hash3 = std::hash<int>{}(std::get<2>(t));
        return hash1 ^ (hash2 << 1) ^ (hash3 << 2);
    }
};

class Router {
private:
    int threshold = 0;
    deque<int> q;
    unordered_map<int, deque<pair<int, int>>> hashmap;
    unordered_set<tuple<int, int, int>, TupleHash> hashset;
public:
    Router(int memoryLimit) {
        threshold = memoryLimit;
    }

    bool addPacket(int source, int destination, int timestamp) {
        tuple<int, int, int> triple = {source, destination, timestamp};
        if (hashset.count(triple)) return false;
        if (q.size() == threshold) {
            int dstn = q.front();
            int scr = hashmap[dstn][0].first;
            int tmstmp = hashmap[dstn][0].second;
            hashset.erase({scr, dstn, tmstmp});
            hashmap[dstn].pop_front();
            q.pop_front();
        }
        hashset.insert(triple);
        hashmap[destination].push_back({source, timestamp});
        q.push_back(destination);
        return true;
    }

    vector<int> forwardPacket() {
        if (q.empty()) return vector<int>();
        int destination = q.front();
        int source = hashmap[destination][0].first;
        int timestamp = hashmap[destination][0].second;

        hashset.erase({source, destination, timestamp});
        hashmap[destination].pop_front();
        q.pop_front();
        return vector<int>{source, destination, timestamp};
    }

    int getCount(int destination, int startTime, int endTime) {
        if (!hashmap.count(destination) || hashmap[destination].empty()) return 0;
        if ((hashmap[destination][0].second > endTime) || (hashmap[destination][hashmap[destination].size() - 1].second < startTime)) return 0;
        int x = 0, y = 0;
        int left = 0, right = hashmap[destination].size() - 1;
        while (left <= right) {
            int middle = left + ((right - left) >> 1);
            if (hashmap[destination][middle].second >= startTime) {
                x = middle;
                right = middle - 1;
            } else left = middle + 1;
        }
        left = 0;
        right = hashmap[destination].size() - 1;
        while (left <= right) {
            int middle = left + ((right - left) >> 1);
            if (hashmap[destination][middle].second <= endTime) {
                y = middle;
                left = middle + 1;
            } else right = middle - 1;
        }
        return y - x + 1;

    }
};

/**
 * Your Router object will be instantiated and called as such:
 * Router* obj = new Router(memoryLimit);
 * bool param_1 = obj->addPacket(source,destination,timestamp);
 * vector<int> param_2 = obj->forwardPacket();
 * int param_3 = obj->getCount(destination,startTime,endTime);
 */

# Python
# addPacket -> O(1)
# forwardPacket -> O(1)
# getCount -> O(logN)
# Memory Complexity O(N)
# DoubleEndedQueue HashMap HashSet BinarySearch
class Router:

    def __init__(self, memoryLimit: int):
        self.q: list[int] = deque()
        self.hashmap: dict[int, list[tuple[int, int]]] = dict()
        self.hashset: set[tuple[int, int, int]] = set()
        self.threshold: int = memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.hashset: return False
        if len(self.q) == self.threshold:
            self.hashmap[self.q.popleft()].popleft()
        if destination not in self.hashmap:
            self.hashmap[destination] = deque()

        self.hashmap[destination].append((source, timestamp))
        self.q.append(destination)
        self.hashset.add((source, destination, timestamp))
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q: return []
        destination: int = self.q.popleft()
        source, timestamp = self.hashmap[destination].popleft()
        self.hashset.remove((source, destination, timestamp))
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.hashmap: return 0
        if not self.hashmap[destination] or self.hashmap[destination][-1][1] < startTime or \
                self.hashmap[destination][0][1] > endTime: return 0
        x = y = 0
        left: int = 0
        right: int = len(self.hashmap[destination]) - 1
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            if self.hashmap[destination][middle][1] >= startTime:
                right = middle - 1
                x = middle
            else:
                left = middle + 1
        left = 0
        right = len(self.hashmap[destination]) - 1
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            if self.hashmap[destination][middle][1] <= endTime:
                left = middle + 1
                y = middle
            else:
                right = middle - 1
        return y - x + 1

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)