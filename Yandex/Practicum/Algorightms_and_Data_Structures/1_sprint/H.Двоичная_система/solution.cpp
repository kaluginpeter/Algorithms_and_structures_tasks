#include <iostream>
#include <string>


void solution(std::string& x, std::string& y) {
    /*
    Time Complexity O(N), where N is the length of place values of the largest number
    Memory Complexity O(N), where N is the length of place values of the largest number
    */
    int xN = x.size(), yN = y.size();
    if (x.size() < y.size()) {
        std::string temp = x;
        int tempN = xN;
        x = y;
        xN = yN;
        y = temp;
        yN = tempN;
    }
    std::string digits = "";
    int yIdx = yN - 1;
    int additional = 0;
    for (int xIdx = xN - 1; xIdx >= 0; --xIdx) {
        if (yIdx >= 0) {
            int bits = (x[xIdx] == '0'? 0 : 1) + (y[yIdx] == '0'? 0 : 1);
            if (additional) {
                ++bits;
                --additional;
            }
            if (bits > 1) {
                ++additional;
                digits += (bits == 3? '1' : '0');
            } else {
                digits += std::to_string(bits);
            }
            --yIdx;
        } else if (additional) {
            int bits = (x[xIdx] == '0'? 0 : 1) + additional;
            --additional;
            if (bits == 2) {
                ++additional;
                digits += '0';
            } else {
                digits += std::to_string(bits);
            }
        } else {
            digits += x[xIdx];
        }
    }
    if (additional) {
        digits += '1';
    }
    int n = digits.size();
    for (int index = n - 1; index >= 0; --index) {
        std::cout << digits[index];
    }
    std::cout << "\n";
};


int main() {
    std::string x, y;
    std::cin >> x >> y;
    solution(x, y);
}
