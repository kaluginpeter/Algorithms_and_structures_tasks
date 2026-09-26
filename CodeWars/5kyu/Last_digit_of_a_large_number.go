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