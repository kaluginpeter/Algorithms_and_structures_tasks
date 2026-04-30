/*
Preface
Billy is tired of his job. He thinks that his boss is rude and his pay is pathetic. Yesterday he found out about forex trading. Now he looks at the charts and fantasizes about becoming a trader and how much money he would make.

Task
Write a function that accepts a list of price points on the chart and returns the maximum possible profit from trading.

Example
ideal_trader([1.0, 1.0, 1.2, 0.8, 0.9, 1.0]) -> 1.5
Let's say that our ideal trader has x dollars on his deposit before he starts trading.

Here's what he does with it:

He uses all his money to buy at 1.0.
He sells everything at 1.2, taking a 20% profit. His deposit is now worth 1.2x
He uses all his money to buy again at 0.8.
He sells everything at 1.0, taking a 25% profit. His deposit is now worth 1.5x
So, during this session, an ideal trader would turn x dollars into 1.5x dollars.

Input
The input list of prices:

Always contains at least two price points.
Contains only positive prices.
Can contain repeating prices (like 1.0, 1.0 in the example).
Additional notes for traders
You should assume that in Billy's fantasies:

There are no broker commissions.
No leverage is used, including shorting (Billy doesn't know about this stuff yet, good for him).
He can always buy or sell exactly at the current price (there is no price slippage).
Orders are executed instantly (before the price changes).
An early version of this kata allowed shorting, but shorts got removed because of issues (see discussion). Some old C/C++/Python solutions are invalid now.

ArraysFundamentals
*/
// Solution
#include <vector>

double ideal_trader(const std::vector<double>& prices)
{
    double output = 1.0, cur = prices[0];
    for (const double& price : prices) {
        if (price > cur) output *= price / cur;
        cur = price;
    }
    return output;
}