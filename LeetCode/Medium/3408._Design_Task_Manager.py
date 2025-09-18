# There is a task management system that allows users to manage their tasks, each associated with a priority. The system should efficiently handle adding, modifying, executing, and removing tasks.
#
# Implement the TaskManager class:
#
# TaskManager(vector<vector<int>>& tasks) initializes the task manager with a list of user-task-priority triples. Each element in the input list is of the form [userId, taskId, priority], which adds a task to the specified user with the given priority.
#
# void add(int userId, int taskId, int priority) adds a task with the specified taskId and priority to the user with userId. It is guaranteed that taskId does not exist in the system.
#
# void edit(int taskId, int newPriority) updates the priority of the existing taskId to newPriority. It is guaranteed that taskId exists in the system.
#
# void rmv(int taskId) removes the task identified by taskId from the system. It is guaranteed that taskId exists in the system.
#
# int execTop() executes the task with the highest priority across all users. If there are multiple tasks with the same highest priority, execute the one with the highest taskId. After executing, the taskId is removed from the system. Return the userId associated with the executed task. If no tasks are available, return -1.
#
# Note that a user may be assigned multiple tasks.
#
#
#
# Example 1:
#
# Input:
# ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"]
# [[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]
#
# Output:
# [null, null, null, 3, null, null, 5]
#
# Explanation
#
# TaskManager taskManager = new TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]]); // Initializes with three tasks for Users 1, 2, and 3.
# taskManager.add(4, 104, 5); // Adds task 104 with priority 5 for User 4.
# taskManager.edit(102, 8); // Updates priority of task 102 to 8.
# taskManager.execTop(); // return 3. Executes task 103 for User 3.
# taskManager.rmv(101); // Removes task 101 from the system.
# taskManager.add(5, 105, 15); // Adds task 105 with priority 15 for User 5.
# taskManager.execTop(); // return 5. Executes task 105 for User 5.
#
#
# Constraints:
#
# 1 <= tasks.length <= 105
# 0 <= userId <= 105
# 0 <= taskId <= 105
# 0 <= priority <= 109
# 0 <= newPriority <= 109
# At most 2 * 105 calls will be made in total to add, edit, rmv, and execTop methods.
# The input is generated such that taskId will be valid.There is a task management system that allows users to manage their tasks, each associated with a priority. The system should efficiently handle adding, modifying, executing, and removing tasks.
#
# Implement the TaskManager class:
#
# TaskManager(vector<vector<int>>& tasks) initializes the task manager with a list of user-task-priority triples. Each element in the input list is of the form [userId, taskId, priority], which adds a task to the specified user with the given priority.
#
# void add(int userId, int taskId, int priority) adds a task with the specified taskId and priority to the user with userId. It is guaranteed that taskId does not exist in the system.
#
# void edit(int taskId, int newPriority) updates the priority of the existing taskId to newPriority. It is guaranteed that taskId exists in the system.
#
# void rmv(int taskId) removes the task identified by taskId from the system. It is guaranteed that taskId exists in the system.
#
# int execTop() executes the task with the highest priority across all users. If there are multiple tasks with the same highest priority, execute the one with the highest taskId. After executing, the taskId is removed from the system. Return the userId associated with the executed task. If no tasks are available, return -1.
#
# Note that a user may be assigned multiple tasks.
#
#
#
# Example 1:
#
# Input:
# ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"]
# [[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]
#
# Output:
# [null, null, null, 3, null, null, 5]
#
# Explanation
#
# TaskManager taskManager = new TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]]); // Initializes with three tasks for Users 1, 2, and 3.
# taskManager.add(4, 104, 5); // Adds task 104 with priority 5 for User 4.
# taskManager.edit(102, 8); // Updates priority of task 102 to 8.
# taskManager.execTop(); // return 3. Executes task 103 for User 3.
# taskManager.rmv(101); // Removes task 101 from the system.
# taskManager.add(5, 105, 15); // Adds task 105 with priority 15 for User 5.
# taskManager.execTop(); // return 5. Executes task 105 for User 5.
#
#
# Constraints:
#
# 1 <= tasks.length <= 105
# 0 <= userId <= 105
# 0 <= taskId <= 105
# 0 <= priority <= 109
# 0 <= newPriority <= 109
# At most 2 * 105 calls will be made in total to add, edit, rmv, and execTop methods.
# The input is generated such that taskId will be valid.
# Solution
# Python O(NlogN) O(N) AVL-Tree HashMap
from sortedcontainers import SortedList
class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.pool: list[tuple[int, int, int]] = SortedList()
        self.tasks: dict[int, tuple[int, int, int]] = dict()
        for task in tasks:
            user_id, task_id, priority = task
            self.pool.add((priority, task_id, user_id))
            self.tasks[task_id] = (priority, task_id, user_id)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.pool.add((priority, taskId, userId))
        self.tasks[taskId] = (priority, taskId, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        triplet: tuple[int, int, int] = self.tasks[taskId]
        self.pool.discard(triplet)
        self.pool.add((newPriority, triplet[1], triplet[2]))
        self.tasks[taskId] = (newPriority, triplet[1], triplet[2])

    def rmv(self, taskId: int) -> None:
        triplet: tuple[int, int, int] = self.tasks[taskId]
        del self.tasks[taskId]
        self.pool.discard(triplet)

    def execTop(self) -> int:
        if not self.pool:
            return -1
        triplet: tuple[int, int, int] = self.pool[-1]
        self.pool.discard(triplet)
        del self.tasks[triplet[1]]
        return triplet[-1]


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()

# C++ O(NlogN) O(N) AVL-Tree HashMap
class TaskManager {
public:
    std::set<std::tuple<int, int, int>> pool;
    std::unordered_map<int, std::tuple<int, int, int>> taskIDs;

    TaskManager(vector<vector<int>>& tasks) {
        for (std::vector<int>& task : tasks) {
            std::tuple<int, int, int> triple = {task[2], task[1], task[0]};
            pool.insert(triple);
            taskIDs[task[1]] = triple;
        }
    }

    void add(int userId, int taskId, int priority) {
        std::tuple<int, int, int> triple = {priority, taskId, userId};
        pool.insert(triple);
        taskIDs[taskId] = triple;
    }

    void edit(int taskId, int newPriority) {
        std::tuple<int, int, int> triple = taskIDs[taskId];
        pool.erase(triple);
        pool.insert({newPriority, std::get<1>(triple), std::get<2>(triple)});
        taskIDs[taskId] = {newPriority, std::get<1>(triple), std::get<2>(triple)};
    }

    void rmv(int taskId) {
        std::tuple<int, int, int> triple = taskIDs[taskId];
        pool.erase(triple);
        taskIDs.erase(taskId);
    }

    int execTop() {
        if (!pool.size()) {
            return -1;
        }
        std::tuple<int, int, int> triple = *pool.rbegin();
        pool.erase(triple);
        taskIDs.erase(std::get<1>(triple));
        return std::get<2>(triple);
    }
};

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager* obj = new TaskManager(tasks);
 * obj->add(userId,taskId,priority);
 * obj->edit(taskId,newPriority);
 * obj->rmv(taskId);
 * int param_4 = obj->execTop();
 */


# Python O(NlogN) O(N) OrderedSet Design
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.overall: list[tuple[int, int]] = SortedList()
        self.task_to_user: dict[int, int] = defaultdict(int)
        self.task_to_priority: dict[int, int] = defaultdict(int)
        for t in tasks:
            self.overall.add((-t[2], -t[1]))
            self.task_to_user[t[1]] = t[0]
            self.task_to_priority[t[1]] = t[2]

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_to_user[taskId] = userId
        self.task_to_priority[taskId] = priority
        self.overall.add((-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.overall.remove((-self.task_to_priority[taskId], -taskId))
        self.overall.add((-newPriority, -taskId))
        self.task_to_priority[taskId] = newPriority

    def rmv(self, taskId: int) -> None:
        self.overall.remove((-self.task_to_priority[taskId], -taskId))
        del self.task_to_priority[taskId]
        del self.task_to_user[taskId]

    def execTop(self) -> int:
        if not self.overall: return -1
        top: tuple[int, int] = self.overall[0]
        self.overall.remove(top)
        del self.task_to_priority[-top[1]]
        user: int = self.task_to_user[-top[1]]
        del self.task_to_user[-top[1]]
        return user


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()

# C++ O(NlogN) O(N) Design OrderedSet
class TaskManager {
private:
    std::unordered_map<int, int> taskToPriority, taskToUser;
    std::set<std::pair<int, int>> overall;
public:
    TaskManager(vector<vector<int>>& tasks) {
        for (vector<int>& t : tasks) {
            taskToUser[t[1]] = t[0];
            taskToPriority[t[1]] = t[2];
            overall.insert({-t[2], -t[1]});
        }
    }

    void add(int userId, int taskId, int priority) {
        taskToUser[taskId] = userId;
        taskToPriority[taskId] = priority;
        overall.insert({-priority, -taskId});
    }

    void edit(int taskId, int newPriority) {
        overall.erase({-taskToPriority[taskId], -taskId});
        overall.insert({-newPriority, -taskId});
        taskToPriority[taskId] = newPriority;
    }

    void rmv(int taskId) {
        overall.erase({-taskToPriority[taskId], -taskId});
        taskToUser.erase(taskId);
        taskToPriority.erase(taskId);
    }

    int execTop() {
        if (overall.empty()) return -1;
        std::pair<int, int> top = *overall.begin();
        overall.erase(top);
        taskToPriority.erase(-top.second);
        int userId = taskToUser[-top.second];
        taskToUser.erase(-top.second);
        return userId;
    }
};

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager* obj = new TaskManager(tasks);
 * obj->add(userId,taskId,priority);
 * obj->edit(taskId,newPriority);
 * obj->rmv(taskId);
 * int param_4 = obj->execTop();
 */