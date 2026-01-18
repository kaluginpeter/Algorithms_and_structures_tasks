/*
You're a fantastic woodworker and you love to make picture frames. You want to know exactly what length of trim will be required in order to make a specified frame.

You are given the inside height and length of the desired frame as well as the width of the trim. We will assume you have the best blade ever made, to cut the wood up. It's so good, the blade has no width, so it doesn't remove any extra material with each cut.

Since you want the frame to look good, you'll be cutting 45° miter joints on each piece.

Frame

You will receive an array of measurements in the following order:

[height, length, width]
The measurements are going to be given to you in string format with some examples below:

[`1' 2 3/8"`, `1' 6"`, `1"`]
[`4"`, `1 1/2"`, `5/32"`]
Your job is to return a string that gives the length of trim required. We will use normal measuring tape denominations of 2,4,8,16,32 if any fractions are needed. Remember that the interior edge must be from the same side of the trim.

Expected Output Format:
Like the input, your output should show any feet followed by the ' symbol then any inches including the fractions followed by the " symbol. Use the lowest denominator for the fraction (i.e. 1/2 instead of 16/32). For those not familiar with imperial measurements, 12" = 1'.

FundamentalsRegular ExpressionsStrings
*/