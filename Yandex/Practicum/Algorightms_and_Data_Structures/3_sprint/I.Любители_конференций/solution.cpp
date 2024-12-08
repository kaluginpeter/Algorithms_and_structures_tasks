#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>


void solution(int& n, std::vector<int>& universitiesId, int& k) {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    */
    std::unordered_map<int, int> hashmap;
    for (int& universityId : universitiesId) {
        ++hashmap[universityId];
    }
    std::vector<int> distinctUniversitiesId;
    for (auto& pair : hashmap) {
        distinctUniversitiesId.push_back(pair.first);
    }
    std::sort(
        distinctUniversitiesId.begin(),
        distinctUniversitiesId.end(),
        [&hashmap](const int& x, const int& y) {
            if (hashmap[x] != hashmap[y]) {
                return hashmap[x] > hashmap[y];
            }
            return -x > -y;
        }
    );
    int dn = distinctUniversitiesId.size();
    for (int idx = 0; idx < std::min(dn, k); ++idx) {
        if (idx) {
            std::cout << " ";
        }
        std::cout << distinctUniversitiesId[idx];
    }
    std::cout << "\n";
}


int main() {
    int n;
    std::cin >> n;
    std::vector<int> universitiesId;
    for (int i = 0; i < n; ++i) {
        int universityId;
        std::cin >> universityId;
        universitiesId.push_back(universityId);
    }
    int k;
    std::cin >> k;
    solution(n, universitiesId, k);
}