# You are given an integer n indicating there are n people numbered from 0 to n - 1. You are also given a 0-indexed 2D integer array meetings where meetings[i] = [xi, yi, timei] indicates that person xi and person yi have a meeting at timei. A person may attend multiple meetings at the same time. Finally, you are given an integer firstPerson.
#
# Person 0 has a secret and initially shares the secret with a person firstPerson at time 0. This secret is then shared every time a meeting takes place with a person that has the secret. More formally, for every meeting, if a person xi has the secret at timei, then they will share the secret with person yi, and vice versa.
#
# The secrets are shared instantaneously. That is, a person may receive the secret and share it with people in other meetings within the same time frame.
#
# Return a list of all the people that have the secret after all the meetings have taken place. You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1
# Output: [0,1,2,3,5]
# Explanation:
# At time 0, person 0 shares the secret with person 1.
# At time 5, person 1 shares the secret with person 2.
# At time 8, person 2 shares the secret with person 3.
# At time 10, person 1 shares the secret with person 5.​​​​
# Thus, people 0, 1, 2, 3, and 5 know the secret after all the meetings.
# Example 2:
#
# Input: n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3
# Output: [0,1,3]
# Explanation:
# At time 0, person 0 shares the secret with person 3.
# At time 2, neither person 1 nor person 2 know the secret.
# At time 3, person 3 shares the secret with person 0 and person 1.
# Thus, people 0, 1, and 3 know the secret after all the meetings.
# Example 3:
#
# Input: n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1
# Output: [0,1,2,3,4]
# Explanation:
# At time 0, person 0 shares the secret with person 1.
# At time 1, person 1 shares the secret with person 2, and person 2 shares the secret with person 3.
# Note that person 2 can share the secret at the same time as receiving it.
# At time 2, person 3 shares the secret with person 4.
# Thus, people 0, 1, 2, 3, and 4 know the secret after all the meetings.
#
#
# Constraints:
#
# 2 <= n <= 105
# 1 <= meetings.length <= 105
# meetings[i].length == 3
# 0 <= xi, yi <= n - 1
# xi != yi
# 1 <= timei <= 105
# 1 <= firstPerson <= n - 1
# Solution
# Python O(E + ElogE + (V + E) + V) O(V + E) Graph Depth-First-Search Sorting
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph: dict[int, list[tuple[int, int]]] = dict()
        for u, v, t in meetings:
            if u not in graph: graph[u] = []
            if v not in graph: graph[v] = []
            graph[u].append((t, v))
            graph[v].append((t, u))
        for vertex, edges in graph.items(): edges.sort()
        was_death: list[int] = [float('inf')] * n
        was_death[0] = 0
        was_death[firstPerson] = 0
        q: list[tuple[int, int]] = [(0, 0), (firstPerson, 0)]
        while q:
            zomby, infected_at = q.pop()
            for meeting, victum in graph.get(zomby, []):
                if infected_at <= meeting and meeting < was_death[victum]:
                    was_death[victum] = meeting
                    q.append((victum, meeting))
        return [victum for victum in range(n) if was_death[victum] != float('inf')]

# C++ O(E + ElogE + (V + E) + V) O(V + E) Sorting Depth-First-Search Graph
class Solution {
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        std::unordered_map<int, std::vector<std::pair<int, int>>> graph;
        for (auto& meeting : meetings) {
            int u = meeting[0], v = meeting[1], t = meeting[2];
            graph[v].emplace_back(t, u);
            graph[u].emplace_back(t, v);
        }
        for (auto& p : graph) std::sort(p.second.begin(), p.second.end());
        std::vector<int> secretAt(n, INT_MAX);
        secretAt[0] = 0;
        secretAt[firstPerson] = 0;
        std::queue<std::pair<int, int>> q;
        q.emplace(0, 0);
        q.emplace(firstPerson, 0);
        while (!q.empty()) {
            auto [person, known] = q.front();
            q.pop();
            for (auto [meetingTime, nextPerson] : graph[person]) {
                if (known <= meetingTime && meetingTime < secretAt[nextPerson]) {
                    secretAt[nextPerson] = meetingTime;
                    q.emplace(nextPerson, meetingTime);
                }
            }
        }
        std::vector<int> output;
        for (int i = 0; i < n; ++i) {
            if (secretAt[i] != INT_MAX) output.push_back(i);
        }
        return output;
    }
};