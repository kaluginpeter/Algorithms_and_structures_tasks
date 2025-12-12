# You are given an integer numberOfUsers representing the total number of users and an array events of size n x 3.
#
# Each events[i] can be either of the following two types:
#
# Message Event: ["MESSAGE", "timestampi", "mentions_stringi"]
# This event indicates that a set of users was mentioned in a message at timestampi.
# The mentions_stringi string can contain one of the following tokens:
# id<number>: where <number> is an integer in range [0,numberOfUsers - 1]. There can be multiple ids separated by a single whitespace and may contain duplicates. This can mention even the offline users.
# ALL: mentions all users.
# HERE: mentions all online users.
# Offline Event: ["OFFLINE", "timestampi", "idi"]
# This event indicates that the user idi had become offline at timestampi for 60 time units. The user will automatically be online again at time timestampi + 60.
# Return an array mentions where mentions[i] represents the number of mentions the user with id i has across all MESSAGE events.
#
# All users are initially online, and if a user goes offline or comes back online, their status change is processed before handling any message event that occurs at the same timestamp.
#
# Note that a user can be mentioned multiple times in a single message event, and each mention should be counted separately.
#
#
#
# Example 1:
#
# Input: numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]
#
# Output: [2,2]
#
# Explanation:
#
# Initially, all users are online.
#
# At timestamp 10, id1 and id0 are mentioned. mentions = [1,1]
#
# At timestamp 11, id0 goes offline.
#
# At timestamp 71, id0 comes back online and "HERE" is mentioned. mentions = [2,2]
#
# Example 2:
#
# Input: numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]
#
# Output: [2,2]
#
# Explanation:
#
# Initially, all users are online.
#
# At timestamp 10, id1 and id0 are mentioned. mentions = [1,1]
#
# At timestamp 11, id0 goes offline.
#
# At timestamp 12, "ALL" is mentioned. This includes offline users, so both id0 and id1 are mentioned. mentions = [2,2]
#
# Example 3:
#
# Input: numberOfUsers = 2, events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]
#
# Output: [0,1]
#
# Explanation:
#
# Initially, all users are online.
#
# At timestamp 10, id0 goes offline.
#
# At timestamp 12, "HERE" is mentioned. Because id0 is still offline, they will not be mentioned. mentions = [0,1]
#
#
#
# Constraints:
#
# 1 <= numberOfUsers <= 100
# 1 <= events.length <= 100
# events[i].length == 3
# events[i][0] will be one of MESSAGE or OFFLINE.
# 1 <= int(events[i][1]) <= 105
# The number of id<number> mentions in any "MESSAGE" event is between 1 and 100.
# 0 <= <number> <= numberOfUsers - 1
# It is guaranteed that the user id referenced in the OFFLINE event is online at the time the event occurs.
# Solution
# Python O(NlogN + MN) O(N) Counting
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda event: (int(event[1]), event[0] != "OFFLINE"))
        users: list[int] = [0] * numberOfUsers
        online: list[int] = [0] * numberOfUsers
        for type_, tmstmp, seq in events:
            tmstmp = int(tmstmp)
            if type_ == "OFFLINE": online[int(seq)] = tmstmp + 60
            else:
                tmstmp = tmstmp if seq == "HERE" else float("inf")
                seq = range(numberOfUsers) if seq in {"HERE", "ALL"} else [int(i[2:]) for i in seq.split()]
                for i in seq:
                    if online[i] > tmstmp: continue
                    users[i] += 1
        return users

# C++ O(NlogN + MN) O(N) Counting
class Solution {
public:
    std::vector<int> getIds(std::string& seq) {
        std::vector<int> ids;
        std::stringstream strm(seq);
        std::string temp;
        while(getline(strm, temp, ' ')) {
            ids.push_back(std::stoi(temp.substr(2)));
        }
        return ids;
    }
    vector<int> countMentions(int numberOfUsers, vector<vector<string>>& events) {
        std::sort(events.begin(), events.end(), [](const std::vector<std::string>& x, const std::vector<std::string>& y) {
            if (x[1] != y[1]) return std::stoi(x[1]) < std::stoi(y[1]);
            return x[0] == "OFFLINE";
        });
        std::vector<int> users(numberOfUsers, 0);
        std::vector<int> onlineSince(numberOfUsers, 0);
        for (std::vector<std::string>& event : events) {
            if (event[0] == "MESSAGE") {
                int tstmp = std::stoi(event[1]);
                if (event[2] == "HERE" || event[2] == "ALL") {
                    tstmp = (event[2] == "HERE" ? tstmp : INT32_MAX);
                    for (int i = 0; i < numberOfUsers; ++i) {
                        if (onlineSince[i] > tstmp) continue;
                        ++users[i];
                    }
                    continue;
                }
                tstmp = INT32_MAX;
                std::vector<int> ids = getIds(event[2]);
                for (int& user : ids) {
                    if (onlineSince[user] > tstmp) continue;
                    ++users[user];
                }
            } else {
                int tstmp = std::stoi(event[1]);
                int user = std::stoi(event[2]);
                onlineSince[user] = tstmp + 60;
            }
        }
        return users;
    }
};