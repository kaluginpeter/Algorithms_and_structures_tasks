# You have a secret message for your friends. You want to mail it to them. But, you are well aware that each of their mail carriers reads their mail before delivering it. So, instead of sending the entire message, you only send some characters to each of them.
#
# If you have n friends, friend 1 gets character 1, n + 1, 2n + 1, etc. And friend 2 gets character 2, n + 2, 2n + 2, etc. All other characters are replaced with dashes.
#
# Example:  3 friends, message: I think you are all sexy
# Friend 1 receives: I--h--k--o--a-- --l--e--
# Friend 2 receives: - --i-- --u--r--a-- --x-
# Friend 3 receives: --t--n--y-- --e--l--s--y
# Treat null messages as empty strings (C#, JavaScript). If your number of friends is greater than the length of your message, some friends will simply receive all dashes. If you have zero friends (or less than zero), return null (empty vector for C++);
#
# FUNDAMENTALS
# Solution
# Python
def split_message(message, count):
    if count <= 0: return None
    friends: list[str] = []
    words: list[str] = list(message)
    for friend in range(count):
        friend_part: list[str] = []
        friend_idx: int = friend
        for idx in range(len(words)):
            if idx == friend_idx:
                friend_part.append(words[idx])
                words[idx] = '-'
                friend_idx += count
            else:
                friend_part.append('-')
        friends.append(''.join(friend_part))
    return friends

# C++
#include <string>
#include <vector>

std::vector<std::string> splitMessage(std::string message, int count)
{
    std::vector<std::string> result;
    for (int frnd = 0; frnd < count; ++frnd) {
      std::string friend_part = "";
      int friend_idx = frnd;
      for (size_t idx = 0; idx < message.size(); ++idx) {
        if (idx == static_cast<size_t>(friend_idx)) {
          friend_part += message[idx];
          message[idx] = '-';
          friend_idx += count;
        } else {
          friend_part += '-';
        }
      }
      result.push_back(friend_part);
    }
    return result;
}