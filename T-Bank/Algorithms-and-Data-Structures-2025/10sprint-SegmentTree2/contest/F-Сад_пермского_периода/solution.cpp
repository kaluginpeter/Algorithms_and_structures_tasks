#include <algorithm>
#include <functional>
#include <iostream>
#include <vector>

struct Center {
    long long x;
    long long y;
    int id;
};

void solution() {
    int n;
    std::scanf("%*d %*d %d", &n);
    std::vector<Center> centers(n);
    for (int id = 0; id < n; ++id) {
        double x, y;
        std::scanf("%lf %lf", &x, &y);
        centers[id] = Center{(long long)(x * 2), (long long)(y * 2), id};
    }
    std::vector<long long> y(n);
    for (int i = 0; i < n; ++i) y[i] = centers[i].y;
    std::sort(y.begin(), y.end());
    y.erase(std::unique(y.begin(), y.end()), y.end());
    std::vector<long long> x(y.size(), 0);
    std::function<long long(int)> getX = [&](int index) {
        long long sum = 0;
        for (; index >= 0; index = (index & (index + 1)) - 1) {
            sum += x[index];
        }
        return sum;
    };
    std::function<void(int, long long)> addSinceX = [&](int index, long long extra) {
        for (; index < (int)x.size(); index = index | (index + 1)) {
            x[index] += extra;
        }
    };
    std::function<void(int, int, long long)> addRangeX = [&](int first, int after, long long extra) {
        addSinceX(first, extra);
        addSinceX(after, -extra);
    };
    std::sort(centers.begin(), centers.end(), [](const Center &left, const Center &right) {
        return left.x < right.x;
    });
    std::vector<long long> ans(n, 0);
    for (Center center : centers) {
        auto it = std::lower_bound(y.begin(), y.end(), center.y);
        int index = int(it - y.begin());
        long long dist = center.x - getX(index);
        ans[center.id] = dist;
        it = std::upper_bound(y.begin(), y.end(), center.y - dist);
        int first = int(it - y.begin());
        it = std::upper_bound(y.begin(), y.end(), center.y + dist);
        int after = int(it - y.begin());
        addRangeX(first, after, dist * 2);
    }
    for (long long value : ans) std::printf("%lld ", value);
}

int main() {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    */
    solution();
    
}