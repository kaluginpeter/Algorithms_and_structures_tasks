# You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.
#
# You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.
#
# Return a list of all the recipes that you can create. You may return the answer in any order.
#
# Note that two recipes may contain each other in their ingredients.
#
#
#
# Example 1:
#
# Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
# Output: ["bread"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# Example 2:
#
# Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
# Example 3:
#
# Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich","burger"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
# We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
#
#
# Constraints:
#
# n == recipes.length == ingredients.length
# 1 <= n <= 100
# 1 <= ingredients[i].length, supplies.length <= 100
# 1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
# recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
# All the values of recipes and supplies combined are unique.
# Each ingredients[i] does not contain any duplicate values.
# Solution
# Python O(N + M) O(N + M) Graph Coloring
class Solution:
    def dfs(self, start: int, recipes: list[str], ingredients: list[list[str]], stack: set[str], status: list[int], recipe_to_index: dict[str, int]) -> bool:
        can_cook: bool = True
        for ingredient in ingredients[start]:
            if ingredient in recipe_to_index:
                if status[recipe_to_index[ingredient]] in {-1, 1}:
                    can_cook = False
                    break
                if not status[recipe_to_index[ingredient]]:
                    status[start] = 1
                    can_cook = self.dfs(recipe_to_index[ingredient], recipes, ingredients, stack, status, recipe_to_index)
                    if not can_cook: break
            elif ingredient not in stack:
                can_cook = False
                break

        if not can_cook: status[start] = -1
        else: status[start] = 2
        return can_cook
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n: int = len(recipes)
        status: list[int] = [0] * n
        stack: set[str] = set(supplies)
        recipe_to_index: dict[str, int] = dict((recipes[i], i) for i in range(n))
        for i in range(n):
            if not status[i]: self.dfs(i, recipes, ingredients, stack, status, recipe_to_index)
        return [recipes[i] for i in range(n) if status[i] == 2]

# C++ O(N + M) O(N + M) Graph Coloring
class Solution {
public:
    bool dfs(int start, vector<string>& recipes, vector<vector<string>>& ingredients, unordered_set<string>& stack, vector<int>& status, unordered_map<string, int>& recipeToIndex) {
        bool canCook = true;
        for (string& ingredient : ingredients[start]) {
            if (!stack.count(ingredient) && (recipeToIndex.count(ingredient) && status[recipeToIndex[ingredient]] == -1)) {
                canCook = false;
                break;
            } else if (recipeToIndex.count(ingredient)) {
                if (status[recipeToIndex[ingredient]] == 1) {
                    canCook = false;
                    break;
                }
                status[start] = 1;
                canCook = dfs(recipeToIndex[ingredient], recipes, ingredients, stack, status, recipeToIndex);
                if (!canCook) break;
            } else if (!stack.count(ingredient)) {
                canCook = false;
                break;
            }
        }
        if (!canCook) {
            status[start] = -1;
            return false;
        }
        status[start] = 2;
        return true;
    }
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
        int n = recipes.size();
        vector<int> status (n, 0);
        unordered_map<string, int> recipeToIndex;
        for (int i = 0; i < n; ++i) recipeToIndex[recipes[i]] = i;
        unordered_set<string> stack;
        for (string& supply : supplies) stack.insert(supply);
        for (int i = 0; i < n; ++i) {
            if (!status[i]) dfs(i, recipes, ingredients, stack, status, recipeToIndex);
        }
        vector<string> coocked;
        for (int i = 0; i < n; ++i) {
            if (status[i] == 2) coocked.push_back(recipes[i]);
        }
        return coocked;
    }
};