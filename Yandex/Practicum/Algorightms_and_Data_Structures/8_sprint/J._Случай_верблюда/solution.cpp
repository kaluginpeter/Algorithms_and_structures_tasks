#include <iostream>
#include <string>
#include <unordered_map>
#include <map>

class Trie {
private:
    std::unordered_map<int, Trie*> tree;
    std::map<std::string, int> words;
public:
    Trie() {}

    void insert(std::string& word) {
        Trie* root = this;
        std::string acronym = getAcronim(word);
        if (acronym.empty()) {
            root->tree[91] = new Trie();
            root->tree[91]->words[word] += 1;
            return;
        }
        for (char& letter : acronym) {
            if (root->tree.count((int)letter) == 0) {
                root->tree[(int)letter] = new Trie();
            }
            root = root->tree[(int)letter];
        }
        ++root->words[word];
    }

    std::string getAcronim(std::string& word) {
        std::string output = "";
        for (char& letter : word) {
            if (std::isupper(letter)) output.push_back(letter);
        }
        return output;
    }

    void printQuery(std::string& query) {
        Trie* root = this;
        for (char& letter : query) {
            if (root->tree.count((int)letter) == 0) {
                return;
            }
            root = root->tree[(int)letter];
        }
        std::map<std::string, int> commands;
        fillSet(root,commands);
        for (const auto& p : commands) {
            for (int i = 0; i < p.second; ++i) std::cout << p.first << "\n";
        }
    }

    void fillSet(Trie* root, std::map<std::string, int>& commands) {
        for (const auto& p : root->words) {
            commands[p.first] = p.second;
        }
        for (int idx = 65; idx <= 91; ++idx) {
            if (root->tree.count(idx)) fillSet(root->tree[idx], commands);
        }
    }
};

void solution() {
    /*
    Time Complexity O(N + MNlog(N))
    Memory Complexity O(L)
    */
    int n;
    std::scanf("%d", &n);
    Trie trie;
    for (int i = 0; i < n; ++i) {
        std::string command;
        std::cin >> command;
        trie.insert(command);
    }
    int m;
    std::scanf("%d", &m);
    for (int i = 0; i < m; ++i) {
        std::string query;
        std::cin >> query;
        trie.printQuery(query);
    }
    std::printf("\n");
}

int main() {
    solution();
    return 0;
}
