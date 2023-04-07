// https://codeforces.com/contest/1811/problem/A

#include <bits/stdc++.h>
using namespace std;

int main() {
    int cases, d, d2;
    string num, n, result = "";
    cin >> cases;

    for (int i = 0; i < cases; i++) {
        cin >> d >> n;
        cin >> num;
        for (int x = 0; x < d; x++) {
            if ((int)num[x] < (int)n[0]) {
                result = num.insert(x , n);
                cout << result << endl;
                break;
            }
        }
        if (result == "") {
            cout << num.insert(d , n) << endl;
        }
        result = "";
    }
}