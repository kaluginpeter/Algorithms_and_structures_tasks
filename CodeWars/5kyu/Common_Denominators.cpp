/* Common denominators

You will have a list of rationals in the form

{ {numer_1, denom_1} , ... {numer_n, denom_n} }
or
[ [numer_1, denom_1] , ... [numer_n, denom_n] ]
or
[ (numer_1, denom_1) , ... (numer_n, denom_n) ]
where all numbers are positive ints. You have to produce a result in the form:

(N_1, D) ... (N_n, D)
or
[ [N_1, D] ... [N_n, D] ]
or
[ (N_1', D) , ... (N_n, D) ]
or
{{N_1, D} ... {N_n, D}}
or
"(N_1, D) ... (N_n, D)"
depending on the language (See Example tests) in which D is as small as possible and

N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.
Example:
convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]
Note:
Due to the fact that the first translations were written long ago - more than 6 years - these first translations have only irreducible fractions.

Newer translations have some reducible fractions. To be on the safe side it is better to do a bit more work by simplifying fractions even if they don't have to be.

Note for Bash:
input is a string, e.g "2,4,2,6,2,8" output is then "6 12 4 12 3 12"

FUNDAMENTALSALGORITHMSMATHEMATICS */
// Solution
#include <numeric>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

class Fracts {
public:
    static std::string convertFrac(std::vector<std::vector<unsigned long long>> &lst) {
        unsigned long long D = 1;
        for (const auto& frac : lst) {
            unsigned long long den = frac[1];
            D = (D * (den / std::gcd(D, den)));
        }
        std::ostringstream output;
        for (const auto& frac : lst) {
            unsigned long long num = frac[0];
            unsigned long long den = frac[1];
            output << "(" << (D / den) * num << "," << D << ")";
        }

        return output.str();
    }
};