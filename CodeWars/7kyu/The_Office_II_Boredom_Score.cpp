/*
Every now and then people in the office moves teams or departments. Depending what people are doing with their time they can become more or less boring. Time to assess the current team.

You will be provided with an object(staff) containing the staff names as keys, and the department they work in as values.

Each department has a different boredom assessment score, as follows:

accounts = 1
finance = 2
canteen = 10
regulation = 3
trading = 6
change = 6
IS = 8
retail = 5
cleaning = 4
pissing about = 25

Depending on the cumulative score of the team, return the appropriate sentiment:

<=80: 'kill me now'
< 100 & > 80: 'i can handle this'
100 or over: 'party time!!'

The Office I - Outed
The Office III - Broken Photocopier
The Office IV - Find a Meeting Room
The Office V - Find a Chair

ARRAYSFUNDAMENTALS
*/
// Solution
#include <map>
#include <string>

std::string boredom(const std::map<std::string, std::string> &staff){
    int total = 0;
    for (auto pair : staff) {
      if (pair.second == "accounts") {
          total += 1;
      } else if (pair.second == "finance") {
          total += 2;
      } else if (pair.second == "canteen") {
          total += 10;
      } else if (pair.second == "regulation") {
          total += 3;
      } else if (pair.second == "trading") {
          total += 6;
      } else if (pair.second == "change") {
          total += 6;
      } else if (pair.second == "IS") {
          total += 8;
      } else if (pair.second == "retail") {
          total += 5;
      } else if (pair.second == "cleaning") {
          total += 4;
      } else if (pair.second == "pissing about") {
          total += 25;
      }
    }
    return (total <= 80? "kill me now" : total < 100? "i can handle this" : "party time!!");
}