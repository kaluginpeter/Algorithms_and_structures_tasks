#include <iostream>
#include <tuple>
#include <climits>
#include <cmath>

double f(long long n, double a, double d) {
    return n / 2.0 * (2 * a + (n - 1) * d);
}

std::tuple<char, long long, long long> vertically(long long n, long long m) {
    long long answerCol = LLONG_MAX;
    long long answerDiff = LLONG_MAX;
    long long left = 0;
    long long right = m;

    while (left <= right) {
        long long middle = left + (right - left) / 2;
        double leftSum = f(n, f(middle - 1, 1, 1), static_cast<double>(m * (middle - 1)));
        double rightSum = f(n, f(m - middle + 1, middle, 1), static_cast<double>(m * (m - middle + 1)));        
        double diff = rightSum - leftSum;

        if (std::abs(diff) <= answerDiff) {
            if (std::abs(diff) == answerDiff) answerCol = std::min(answerCol, middle);
            else answerCol = middle;
            answerDiff = std::abs(diff);
        }

        if (diff < 0) right = middle - 1;
        else left = middle + 1;
    }
    return {'V', answerCol, answerDiff};
}

std::tuple<char, long long, long long> horizontally(long long n, long long m) {
    long long answerCol = LLONG_MAX;
    long long answerDiff = LLONG_MAX;
    long long left = 0;
    long long right = n;
    long long mSquare = m * m;

    while (left <= right) {
        long long middle = left + (right - left) / 2;
        double leftSum = (middle > 1 ? f(middle - 1, f(m, 1, 1), static_cast<double>(mSquare)) : 0);
        double rightSum = f(n - middle + 1, f(m, (middle - 1) * m + 1, 1), static_cast<double>(mSquare));
        double diff = rightSum - leftSum;

        if (std::abs(diff) < answerDiff) {
            answerCol = middle;
            answerDiff = std::abs(diff);
        }

        if (diff < 0) right = middle - 1;
        else left = middle + 1;
    }
    return {'H', answerCol, answerDiff};
}

void solution() {
    /*
    Time Complexity O(logN + logM)
    Memory Complexity O(1)
    */
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        long long n, m;
        std::cin >> n >> m;
        auto [row, col, diff] = vertically(n, m);
        auto [gor_row, gor_col, gor_diff] = horizontally(n, m);
        if (gor_diff < diff) {
            row = gor_row;
            col = gor_col;
        }
        std::cout << row << " " << col << "\n";
    }
}

int main() {
    solution();
    return 0;
}
