// https://codeforces.com/problemset/problem/580/A

#include <bits/stdc++.h>
using namespace std;

int longest_increasing_subsequence(vector<int>& arr)
{
    vector<int> ans, sizes;
    int value, n = arr.size();
    
    for (int i = 0; i < n; i++) {
        value = arr[i];
        if (ans.empty()) {
            ans.push_back(arr[i]);
        }
        else if (ans.back() <= value) {
            ans.push_back(arr[i]);
        }
        else {
            sizes.push_back(ans.size());
            ans.clear();
            ans.push_back(arr[i]);
        }
    }
    sizes.push_back(ans.size());
    return *max_element(sizes.begin(), sizes.end());
}


int main() {
    vector<int> numbers;
    int cases, input;
    cin >> cases;

    cin >> input;
    while (cases > 0) {
        numbers.push_back(input);
        cin >> input;
        cases--;
    }

    int ans = longest_increasing_subsequence(numbers);
    cout << ans;
    return 0;
}