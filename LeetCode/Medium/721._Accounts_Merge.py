# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
#
# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
#
#
#
# Example 1:
#
# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and second John's are the same person as they have the common email "johnsmith@mail.com".
# The third John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
# Example 2:
#
# Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
# Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
#
#
# Constraints:
#
# 1 <= accounts.length <= 1000
# 2 <= accounts[i].length <= 10
# 1 <= accounts[i][j].length <= 30
# accounts[i][0] consists of English letters.
# accounts[i][j] (for j > 0) is a valid email.
# Solution
# Python O(NMlog(NM)) O(N + M) Union Find HashMap Sorting
class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents: list[int] = list(range(n))
        self.rank: list[int] = [0] * n

    def union(self, new_owner: int, old_owner: int) -> int:
        root_new_owner: int = self.find(new_owner)
        root_old_owner: int = self.find(old_owner)
        if root_new_owner != root_old_owner:
            if self.rank[root_old_owner] > self.rank[root_new_owner]:
                self.parents[root_new_owner] = root_old_owner
            elif self.rank[root_old_owner] < self.rank[root_new_owner]:
                self.parents[root_old_owner] = root_new_owner
            else:
                self.parents[root_new_owner] = root_old_owner
                self.rank[root_old_owner] += 1

    def find(self, owner: int) -> int:
        while owner != self.parents[owner]:
            self.parents[owner] = self.parents[self.parents[owner]]
            owner = self.parents[owner]
        return owner


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union_find: UnionFind = UnionFind(len(accounts))
        # key: email - value: owner
        ownership: dict[str, int] = dict()
        for owner_idx in range(len(accounts)):
            for account_idx in range(1, len(accounts[owner_idx])):
                if accounts[owner_idx][account_idx] in ownership:
                    # Union owner if email exist
                    union_find.union(owner_idx, ownership[accounts[owner_idx][account_idx]])
                else:
                    ownership[accounts[owner_idx][account_idx]] = owner_idx
        # key: owner_idx - value: list[emails]
        output: dict[int, list[str]] = defaultdict(list)
        for email, owner in ownership.items():
            # find main owner of emails in that group
            output[union_find.find(owner)].append(email)
        return [[accounts[owner_idx][0]] + sorted(emails) for owner_idx, emails in output.items()]