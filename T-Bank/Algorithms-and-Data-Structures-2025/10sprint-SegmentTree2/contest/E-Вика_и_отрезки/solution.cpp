#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

struct Event {
    long long x;
    long long y1, y2;
    int type;
    
    bool operator<(const Event& other) const {
        if (x != other.x) return x < other.x;
        return type > other.type;
    }
};

class SegmentTree {
private:
    vector<int> lazy;
    vector<int> count;
    vector<long long> len;
    vector<long long> y_coords;
    
    void build(int node, int start, int end) {
        lazy[node] = 0;
        count[node] = 0;
        len[node] = 0;
        
        if (start == end) return;
        
        int mid = (start + end) / 2;
        build(2 * node, start, mid);
        build(2 * node + 1, mid + 1, end);
    }
    
    void update(int node, int start, int end, int l, int r, int val) {
        if (start > r || end < l) return;
        
        if (start >= l && end <= r) {
            count[node] += val;
            if (count[node] > 0) {
                len[node] = y_coords[end + 1] - y_coords[start];
            } else {
                if (start == end) {
                    len[node] = 0;
                } else {
                    len[node] = len[2 * node] + len[2 * node + 1];
                }
            }
            return;
        }
        int mid = (start + end) / 2;
        update(2 * node, start, mid, l, r, val);
        update(2 * node + 1, mid + 1, end, l, r, val);
        
        if (count[node] > 0) {
            len[node] = y_coords[end + 1] - y_coords[start];
        } else {
            len[node] = len[2 * node] + len[2 * node + 1];
        }
    }
    
public:
    SegmentTree(const vector<long long>& coords) : y_coords(coords) {
        int n = coords.size() - 1; 
        lazy.resize(4 * n, 0);
        count.resize(4 * n, 0);
        len.resize(4 * n, 0);
        build(1, 0, n - 1);
    }
    
    void update(int l, int r, int val) {
        update(1, 0, y_coords.size() - 2, l, r, val);
    }
    
    long long getLength() {
        return len[1];
    }
};


void solution() {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    */
    int n;
    cin >> n;
    
    vector<Event> events;
    set<long long> y_coords_set;
    
    for (int i = 0; i < n; i++) {
        long long x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        if (x1 > x2) swap(x1, x2);
        if (y1 > y2) swap(y1, y2);
        
        if (y1 == y2) {
            events.push_back({x1, y1, y1 + 1, 1});
            events.push_back({x2 + 1, y1, y1 + 1, -1});
        } else {
            events.push_back({x1, y1, y2 + 1, 1});
            events.push_back({x1 + 1, y1, y2 + 1, -1});
        }
        y_coords_set.insert(y1);
        y_coords_set.insert(y1 + 1);
        if (y1 != y2) {
            y_coords_set.insert(y2);
            y_coords_set.insert(y2 + 1);
        }
    }
    vector<long long> y_coords(y_coords_set.begin(), y_coords_set.end());
    map<long long, int> y_compress;
    for (int i = 0; i < y_coords.size(); i++) {
        y_compress[y_coords[i]] = i;
    }
    
    sort(events.begin(), events.end());
    SegmentTree segTree(y_coords);
    
    long long total_cells = 0;
    long long prev_x = events[0].x;
    
    for (const auto& event : events) {
        long long width = event.x - prev_x;
        total_cells += width * segTree.getLength();
        
        int y1_idx = y_compress[event.y1];
        int y2_idx = y_compress[event.y2] - 1;
        segTree.update(y1_idx, y2_idx, event.type);
        prev_x = event.x;
    }
    
    cout << total_cells << endl;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    solution();
    return 0;
}
