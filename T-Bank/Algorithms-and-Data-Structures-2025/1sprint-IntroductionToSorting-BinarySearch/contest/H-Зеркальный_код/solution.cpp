#include <iostream>
#include <vector>
#include <string>
#include <algorithm>


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    int n;
    std::cin >> n;
    std::string letters;
    std::cin >> letters;
    std::vector<int> chunks(26, 0);
    for (char& letter : letters) {
        ++chunks[letter - 'A'];
    }
    std::string output = "";
    char median = '0';
    for (int i = 0; i < 26; ++i) {
        if (!chunks[i]) continue;
        if ((chunks[i] % 2 != 0) && (median == '0')) median = (char)(i + 65);
        if (chunks[i] / 2)
            for (int j = 0; j < chunks[i] / 2; j++)
                output += (char)(i + 65);
    }
    std::string palindrom = output;
    if (median != '0') palindrom.push_back(median);
    std::reverse(output.begin(), output.end());
    palindrom += output;
    std::cout << palindrom << "\n";
}


int main() {
    solution();
}