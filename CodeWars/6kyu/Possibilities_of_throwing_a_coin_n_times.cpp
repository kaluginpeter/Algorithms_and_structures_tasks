/*
In this kata you will be given an integer n, which is the number of times that a coin is thrown. You will have to return a sorted array of strings for all the possibilities ( heads is 'H', tails is 'T' ).

Examples
n = 1 should return {"H", "T"}
n = 2 should return {"HH", "HT", "TH", "TT"}
n = 3 should return {"HHH", "HHT", "HTH", "HTT", "THH", "THT", "TTH", "TTT"}
In C and C++ just return a char* with all elements separated by , ( no space ):

coin(2) should return "HH,HT,TH,TT"
Input
0 < n < 18

Careful with performance!! You'll have to pass 3 basic test (n = 1, n = 2, n = 3), many medium tests (3 < n <= 10) and many large tests (10 < n < 18)

MathematicsStatisticsPermutationsPerformance
*/
// Solution
void backtrack(int n, std::string& path, std::string& output) {
    if (!n) {
        output += path + ',';
        return;
    }
    path += 'H';
    backtrack(n - 1, path, output);
    path.pop_back();
    path += 'T';
    backtrack(n - 1, path, output);
    path.pop_back();
}

std::string coin(int n) {
    std::string output = "";
    std::string path = "";
    backtrack(n, path, output);
    return output.substr(0, output.size() - 1);
}