# Design a food rating system that can do the following:
#
# Modify the rating of a food item listed in the system.
# Return the highest-rated food item for a type of cuisine in the system.
# Implement the FoodRatings class:
#
# FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.
# foods[i] is the name of the ith food,
# cuisines[i] is the type of cuisine of the ith food, and
# ratings[i] is the initial rating of the ith food.
# void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
# String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.
# Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.
#
#
#
# Example 1:
#
# Input
# ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
# [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
# Output
# [null, "kimchi", "ramen", null, "sushi", null, "ramen"]
#
# Explanation
# FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
# foodRatings.highestRated("korean"); // return "kimchi"
#                                     // "kimchi" is the highest rated korean food with a rating of 9.
# foodRatings.highestRated("japanese"); // return "ramen"
#                                       // "ramen" is the highest rated japanese food with a rating of 14.
# foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
# foodRatings.highestRated("japanese"); // return "sushi"
#                                       // "sushi" is the highest rated japanese food with a rating of 16.
# foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
# foodRatings.highestRated("japanese"); // return "ramen"
#                                       // Both "sushi" and "ramen" have a rating of 16.
#                                       // However, "ramen" is lexicographically smaller than "sushi".
#
#
# Constraints:
#
# 1 <= n <= 2 * 104
# n == foods.length == cuisines.length == ratings.length
# 1 <= foods[i].length, cuisines[i].length <= 10
# foods[i], cuisines[i] consist of lowercase English letters.
# 1 <= ratings[i] <= 108
# All the strings in foods are distinct.
# food will be the name of a food item in the system across all calls to changeRating.
# cuisine will be a type of cuisine of at least one food item in the system across all calls to highestRated.
# At most 2 * 104 calls in total will be made to changeRating and highestRated.
# Solution
from sortedcontainers import SortedList


class FoodRatings(object):
    def __init__(self, foods, cuisines, ratings):
        self.food_dct = {}
        self.csn_dct = defaultdict(SortedList)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_dct[food] = (cuisine, rating)
            self.csn_dct[cuisine].add((-rating, food))

    def changeRating(self, food, newRating):
        cuisine, rating = self.food_dct[food]
        self.food_dct[food] = cuisine, newRating
        self.csn_dct[cuisine].remove((-rating, food))
        self.csn_dct[cuisine].add((-newRating, food))

    def highestRated(self, cuisine):
        return self.csn_dct[cuisine][0][1]


# Python O(NlogN) O(N) HashMap BST
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.hashmap: dict[str, str] = dict()
        self.rating: dict[str, int] = dict()
        self.bst: dict[str, list[tuple[int, str]]] = dict()
        for i in range(len(foods)):
            self.rating[foods[i]] = -ratings[i]
            self.hashmap[foods[i]] = cuisines[i]
            if cuisines[i] not in self.bst: self.bst[cuisines[i]] = SortedList()
            self.bst[cuisines[i]].add((-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.bst[self.hashmap[food]].remove((self.rating[food], food))
        self.bst[self.hashmap[food]].add((-newRating, food))
        self.rating[food] = -newRating

    def highestRated(self, cuisine: str) -> str:
        return self.bst[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

# C++ O(NlogN) O(N) HashMap Red-Black-Tree
class FoodRatings {
private:
    std::unordered_map<std::string, std::string> hashmap;
    std::unordered_map<std::string, int> rating;
    std::unordered_map<std::string, std::set<std::tuple<int, std::string>>> rbt;
public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        for (size_t i = 0; i < foods.size(); ++i) {
            hashmap[foods[i]] = cuisines[i];
            rating[foods[i]] = -ratings[i];
            rbt[cuisines[i]].insert(std::make_tuple(-ratings[i], foods[i]));
        }
    }
    void changeRating(string food, int newRating) {
        rbt[hashmap[food]].erase(std::make_tuple(rating[food], food));
        rbt[hashmap[food]].insert(std::make_tuple(-newRating, food));
        rating[food] = -newRating;
    }

    string highestRated(string cuisine) {
        return std::get<1>(*rbt[cuisine].begin());
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */