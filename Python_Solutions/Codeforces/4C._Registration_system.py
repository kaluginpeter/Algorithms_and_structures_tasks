# C. Registration system
# time limit per test5 seconds
# memory limit per test64 megabytes
# inputstdin
# outputstdout
# A new e-mail service "Berlandesk" is going to be opened in Berland in the near future. The site administration wants to launch their project as soon as possible, that's why they ask you to help. You're suggested to implement the prototype of site registration system. The system should work on the following principle.
#
# Each time a new user wants to register, he sends to the system a request with his name. If such a name does not exist in the system database, it is inserted into the database, and the user gets the response OK, confirming the successful registration. If the name already exists in the system database, the system makes up a new user name, sends it to the user as a prompt and also inserts the prompt into the database. The new name is formed by the following rule. Numbers, starting with 1, are appended one after another to name (name1, name2, ...), among these numbers the least i is found so that namei does not yet exist in the database.
#
# Input
# The first line contains number n (1 ≤ n ≤ 105). The following n lines contain the requests to the system. Each request is a non-empty line, and consists of not more than 32 characters, which are all lowercase Latin letters.
#
# Output
# Print n lines, which are system responses to the requests: OK in case of successful registration, or a prompt with a new name, if the requested name is already taken.
#
# Examples
# inputCopy
# 4
# abacaba
# acaba
# abacaba
# acab
# outputCopy
# OK
# OK
# abacaba1
# OK
# inputCopy
# 6
# first
# first
# second
# second
# third
# third
# outputCopy
# OK
# first1
# OK
# second1
# OK
# third1
# Solution HashTable O(N) O(N)
import sys


def solution(n: int) -> None:
    storage: dict = dict()
    for _ in range(n):
        name: str = sys.stdin.readline().rstrip()
        acc: int = 1
        if name not in storage:
            storage[name] = 0
            print('OK')
        else:
            acc: int = storage[name] + 1
            new_name: str = name + str(acc)
            storage[name] = acc
            storage[new_name] = 0
            print(new_name)


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    solution(n)