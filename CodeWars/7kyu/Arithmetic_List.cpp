/*
In this kata, you will write an arithmetic list which is basically a list that contains consecutive terms in the sequence.
You will be given three parameters :

first the first term in the sequence
c the constant that you are going to ADD ( since it is an arithmetic sequence...)
l the number of terms that should be returned
Useful link: Sequence

Be sure to check out my Arithmetic sequence Kata first ;)
Don't forget about the indexing pitfall ;)

ArraysFundamentals
*/
// Solution
#include <vector>

std::vector<int> seqList(int first, int c, std::size_t l)
{
    std::vector<int> output;
    int x = first;
    for (std::size_t i = 0; i < l; ++i) {
      output.push_back(x);
      x += c;
    }
    return output;
}