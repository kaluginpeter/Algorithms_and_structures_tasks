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


# Python O(1) + O(logD) O(N) Queue BinarySearch HashMap
class Router:

    def __init__(self, memoryLimit: int):
        self.bound: int = memoryLimit
        self.q: list[int] = deque()
        self.d_to_time: dict[int, list[tuple[int, int]]] = defaultdict(deque)
        self.seen: set[tuple[int, int, int]] = set()

    def remove_packet(self) -> None:
        dist: int = self.q.popleft()
        time, source = self.d_to_time[dist].popleft()
        self.seen.remove((source, dist, time))

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        ceil: tuple[int, int, int] = (source, destination, timestamp)
        if ceil in self.seen: return False
        if len(self.q) == self.bound: self.remove_packet()
        self.seen.add(ceil)
        self.q.append(destination)
        self.d_to_time[destination].append((timestamp, source))
        return True

    def forwardPacket(self) -> List[int]:
        output: list[int] = []
        if not self.q: return output
        output.extend(reversed(self.d_to_time[self.q[0]][0]))
        output.append(self.q[0])
        output[-2], output[-1] = output[-1], output[-2]
        self.remove_packet()
        return output

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        left: int = 0
        right: int = 0
        l: int = 0
        r: int = len(self.d_to_time[destination]) - 1
        while l <= r:
            middle: int = l + ((r - l) >> 1)
            if self.d_to_time[destination][middle][0] < startTime:
                l = middle + 1
            else:
                r = middle - 1
        left = l
        l = 0
        r = len(self.d_to_time[destination]) - 1
        while l <= r:
            middle: int = l + ((r - l) >> 1)
            if self.d_to_time[destination][middle][0] > endTime:
                r = middle - 1
            else:
                l = middle + 1
        right = r
        return right - left + 1

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)

# C++ O(1) + O(logD) O(N) Queue HashMap BinarySearch
static inline std::uint64_t splitmix64(std::uint64_t x) {
    x += 0x9e3779b97f4a7c15ULL;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
    x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
    return x ^ (x >> 31);
}

struct TupleHashStrong {
    std::size_t operator()(const std::tuple<int,int,int>& t) const noexcept {
        std::uint64_t h1 = std::hash<int>{}(std::get<0>(t));
        std::uint64_t h2 = std::hash<int>{}(std::get<1>(t));
        std::uint64_t h3 = std::hash<int>{}(std::get<2>(t));
        std::uint64_t res = h1;
        res = splitmix64(res + 0x9e3779b97f4a7c15ULL + (h2<<6) + (h2>>2));
        res ^= splitmix64(h3 + 0x9e3779b97f4a7c15ULL + (res<<6) + (res>>2));
        return static_cast<std::size_t>(res);
    }
};

struct TupleEq {
    bool operator()(const std::tuple<int,int,int>& a,
                    const std::tuple<int,int,int>& b) const noexcept {
        return a == b;
    }
};

class Router {
private:
    std::deque<int> q;
    int bound;
    std::unordered_map<int, std::deque<std::pair<int, int>>> dToTime;
    std::unordered_set<std::tuple<int, int, int>, TupleHashStrong, TupleEq> seen;
public:
    Router(int memoryLimit) {
        bound = memoryLimit;
    }

    void removePacket() {
        std::tuple<int, int, int> ceil = std::make_tuple(dToTime[q.front()].front().second, q.front(), dToTime[q.front()].front().first);
        dToTime[q.front()].pop_front();
        q.pop_front();
        seen.erase(ceil);
    }

    bool addPacket(int source, int destination, int timestamp) {
        std::tuple<int, int, int> ceil = std::make_tuple(source, destination, timestamp);
        if (seen.count(ceil)) return false;
        if (q.size() == bound) removePacket();
        seen.insert(ceil);
        dToTime[destination].push_back(std::make_pair(timestamp, source));
        q.push_back(destination);
        return true;
    }

    vector<int> forwardPacket() {
        std::vector<int> output;
        if (q.empty()) return output;
        output.push_back(dToTime[q.front()].front().second);
        output.push_back(q.front());
        output.push_back(dToTime[q.front()].front().first);
        removePacket();
        return output;
    }

    int getCount(int destination, int startTime, int endTime) {
        if (dToTime[destination].empty()) return 0;
        int left = 0, right = 0, l = 0, r = dToTime[destination].size() - 1;
        while (l <= r) {
            int middle = l + ((r - l) >> 1);
            if (dToTime[destination][middle].first < startTime) l = middle + 1;
            else r = middle - 1;
        }
        left = l;
        l = 0;
        r = dToTime[destination].size() - 1;
        while (l <= r) {
            int middle = l + ((r - l) >> 1);
            if (dToTime[destination][middle].first > endTime) r = middle - 1;
            else l = middle + 1;
        }
        right = r;
        return right - left + 1;
    }
};

/**
 * Your Router object will be instantiated and called as such:
 * Router* obj = new Router(memoryLimit);
 * bool param_1 = obj->addPacket(source,destination,timestamp);
 * vector<int> param_2 = obj->forwardPacket();
 * int param_3 = obj->getCount(destination,startTime,endTime);
 */