# There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.
#
# You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.
#
# Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.
#
#
#
# Example 1:
#
#
# Input: n = 4, connections = [[0,1],[0,2],[1,2]]
# Output: 1
# Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
# Example 2:
#
#
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
# Output: 2
# Example 3:
#
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
# Output: -1
# Explanation: There are not enough cables.
#
#
# Constraints:
#
# 1 <= n <= 105
# 1 <= connections.length <= min(n * (n - 1) / 2, 105)
# connections[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no repeated connections.
# No two computers are connected by more than one cable.
# Solution
# Python O(N) O(N) Union Find
class UnionFind:
    def __init__(self, computers: int) -> None:
        self.connections: int = computers
        self.main: list[int] = list(range(computers))
        self.ethernet_hub: list[int] = [1] * computers

    def find(self, pc: int) -> int:
        while pc != self.main[pc]:
            self.main[pc] = self.main[self.main[pc]]
            pc = self.main[pc]
        return pc

    def unionFind(self, pc1: int, pc2: int) -> bool:
        main_pc1: int = self.find(pc1)
        main_pc2: int = self.find(pc2)
        if main_pc1 == main_pc2:
            return False
        self.connections -= 1
        if self.ethernet_hub[main_pc1] >= self.ethernet_hub[main_pc2]:
            self.main[main_pc2] = main_pc1
            self.ethernet_hub[main_pc1] += self.ethernet_hub[main_pc2]
        else:
            self.main[main_pc1] = main_pc2
            self.ethernet_hub[main_pc2] += self.ethernet_hub[main_pc1]
        return True


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        LAN: UnionFind = UnionFind(n)
        redudant_switches: int = 0
        for switch_hub in connections:
            switch_pc1: int = switch_hub[0]
            switch_pc2: int = switch_hub[1]
            if not LAN.unionFind(switch_pc1, switch_pc2):
                redudant_switches += 1
        needed_switches: int = LAN.connections - 1
        if redudant_switches >= needed_switches:
            return needed_switches
        return -1

# C++ O(N) O(N) Union Find
class UnionFind {
public:
    int connections;
    std::vector<int> main;
    std::vector<int> ethernet_hub;
    UnionFind(int computers) {
        connections = computers;
        main.resize(computers, 0);
        std::iota(main.begin(), main.end(), 0);
        ethernet_hub.resize(computers, 1);
    };

    int find(int pc) {
        while (pc != main[pc]) {
            main[pc] = main[main[pc]];
            pc = main[pc];
        }
        return pc;
    };

    bool unionFind(int pc1, int pc2) {
        int main_pc1 = find(pc1);
        int main_pc2 = find(pc2);
        if (main_pc1 == main_pc2) {
            return false;
        }
        --connections;
        if (ethernet_hub[main_pc1] >= ethernet_hub[main_pc2]) {
            main[main_pc2] = main_pc1;
            ethernet_hub[main_pc1] += ethernet_hub[main_pc2];
        } else {
            main[main_pc1] = main_pc2;
            ethernet_hub[main_pc2] += ethernet_hub[main_pc1];
        }
        return true;
    };
};

class Solution {
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
        UnionFind* LAN = new UnionFind(n);
        int redudant_switches = 0;
        for (std::vector switch_pc_hub : connections) {
            int switch_pc1 = switch_pc_hub[0];
            int switch_pc2 = switch_pc_hub[1];
            if (!LAN->unionFind(switch_pc1, switch_pc2)) {
                ++redudant_switches;
            }
        }
        int needed_switches = LAN->connections - 1;
        if (redudant_switches >= needed_switches) {
            return needed_switches;
        }
        return -1;
    };
};