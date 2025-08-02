/*
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.

StringsFundamentals
*/
// Solution
#include <string>
#include <vector>

std::string likes(const std::vector<std::string> &names)
{
    if (names.empty()) return std::string("no one likes this");
    else if (names.size() == 1) return names[0] + std::string(" likes this");
    else if (names.size() == 2) return names[0] + std::string(" and ") + names[1] + std::string(" like this");
    else if (names.size() == 3) return names[0] + std::string(", ") + names[1] + std::string(" and ") + names[2] + std::string(" like this");
    return names[0] + std::string(", ") + names[1] + std::string(" and ") + std::to_string(names.size() - 2) + std::string(" others like this");
}