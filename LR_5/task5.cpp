#include <iostream>
#include <vector>
using namespace std;

void combineUtil(vector<vector<int>> &res, vector<int> &temp, int n, int start, int k) {
    if (temp.size() == k) {
        res.push_back(temp);
        return;
    }
    for (int i = start; i <= n; ++i) {
        temp.push_back(i);
        combineUtil(res, temp, n, i + 1, k);
        temp.pop_back();
    }
}

vector<vector<int>> getCombinations(int n, int k) {
    vector<vector<int>> res;
    vector<int> temp;
    combineUtil(res, temp, n, 1, k);
    return res;
}

int main() {
    vector<vector<int>> result = getCombinations(3, 2);
    for (const auto &comb : result) {
        for (int num : comb)
            cout << num << " ";
        cout << endl;
    }
    return 0;
}
