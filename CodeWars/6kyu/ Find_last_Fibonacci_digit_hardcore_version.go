/*
Just like in the "father" kata, you will have to return the last digit of the nth element in the Fibonacci sequence (starting with 1,1, to be extra clear, not with 0,1 or other numbers).

You will just get much bigger numbers, so good luck bruteforcing your way through it ;)

LastFibDigit(1) == 1
LastFibDigit(2) == 1
LastFibDigit(3) == 2
LastFibDigit(1000) == 5
LastFibDigit(1000000) == 5
Algorithms
*/
// Solution
package kata


func LastFibDigit(n int) int {
	  return int("011235831459437077415617853819099875279651673033695493257291"[n % 60] - '0')
}