/*
Define a function that takes in two non-negative integers 
a
a and 
b
b and returns the last decimal digit of 
a
b
a 
b
 . Note that 
a
a and 
b
b may be very large!

For example, the last decimal digit of 
9
7
9 
7
  is 
9
9, since 
9
7
=
4782969
9 
7
 =4782969. The last decimal digit of 
(
2
200
)
2
300
(2 
200
 ) 
2 
300
 
 , which has over 
1
0
92
10 
92
  decimal digits, is 
6
6. Also, please take 
0
0
0 
0
  to be 
1
1.

You may assume that the input will always be valid.

Examples
lastDigit 4 1             `shouldBe` 4
lastDigit 4 2             `shouldBe` 6
lastDigit 9 7             `shouldBe` 9
lastDigit 10 (10^10)      `shouldBe` 0
lastDigit (2^200) (2^300) `shouldBe` 6
Remarks
C++, R, PureScript, COBOL
AlgorithmsMathematics
*/
// Solution
package kata

func LastDigit(n1, n2 string) int {
	isZero := true
	for _, c := range n2 {
		if c != '0' {
			isZero = false
			break
		}
	}
	if isZero {
		return 1
	}
	if len(n1) == 0 {
		return 0
	}

	d := int(n1[len(n1)-1] - '0')

	tail := n2
	if len(tail) > 2 {
		tail = tail[len(tail)-2:]
	}
	e := 0
	for _, c := range tail {
		e = e*10 + int(c-'0')
	}
	e %= 4
	if e == 0 {
		e = 4
	}

	r := 1
	for i := 0; i < e; i++ {
		r = r * d % 10
	}
	return r
}