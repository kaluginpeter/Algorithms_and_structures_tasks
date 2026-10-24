/*
Alice and Bob are traveling to Rome for separate business meetings.

You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.

Return the total number of days that Alice and Bob are in Rome together.

You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

 

Example 1:

Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
Output: 3
Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.
Example 2:

Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
Output: 0
Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.
 

Constraints:

All dates are provided in the format "MM-DD".
Alice and Bob's arrival dates are earlier than or equal to their leaving dates.
The given dates are valid dates of a non-leap year.
*/
// Solution
// Go O(1) O(1) Math Greedy
import "strconv"
func countDaysTogether(arriveAlice string, leaveAlice string, arriveBob string, leaveBob string) int {
    var months []int = []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
    aliceStartMonth, _ := strconv.Atoi(arriveAlice[:2])
    aliceStartDay, _ := strconv.Atoi(arriveAlice[3:])
    bobStartMonth, _ := strconv.Atoi(arriveBob[:2])
    bobStartDay, _ := strconv.Atoi(arriveBob[3:])
    var startMonth, startDay int = aliceStartMonth, aliceStartDay
    if (bobStartMonth > startMonth) || (bobStartMonth == startMonth && bobStartDay > startDay) {
        startMonth = bobStartMonth
        startDay = bobStartDay
    }
    aliceEndMonth, _ := strconv.Atoi(leaveAlice[:2])
    aliceEndDay, _ := strconv.Atoi(leaveAlice[3:])
    bobEndMonth, _ := strconv.Atoi(leaveBob[:2])
    bobEndDay, _ := strconv.Atoi(leaveBob[3:])
    var endMonth, endDay int = aliceEndMonth, aliceEndDay
    if (bobEndMonth < endMonth) || (bobEndMonth == endMonth && bobEndDay < endDay) {
        endMonth = bobEndMonth
        endDay = bobEndDay
    }
    var together int = 0
    for i := startMonth; i <= endMonth; i++ {
        together += months[i - 1]
        if i == startMonth { together -= startDay - 1 }
        if i == endMonth { together -= months[i - 1] - endDay }
    }
    return max(0, together)
}