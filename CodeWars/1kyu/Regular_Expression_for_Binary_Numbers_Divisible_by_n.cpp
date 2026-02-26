/*
Regular Expression for Binary Numbers Divisible by n
Create a function that will return a regular expression string that is capable of evaluating binary strings (which consist of only 1s and 0s) and determining whether the given string represents a number divisible by n.

Tests
Inputs 1 <= n <= 18 will be tested

Each n will be tested against random invalid tests and random valid tests (which may or may not pass the regex test itself, accordingly).

Notes
Strings that are not binary numbers should be rejected.
Keep your solution under 5000 characters. This means you can't hard-code the answers.
Only these characters may be included in your returned string:
01?:*+^$()[]|

C++ Notes
The second anti-cheat test checks if you used the STL's regex library in your code.
The macro constant _GLIBCXX_REGEX_STATE_LIMIT which limits the maximum size of a regex has been set to 400000, as the default limit would be too constraining for the larger inputs.
AlgorithmsPuzzlesRegular ExpressionsStrings
*/