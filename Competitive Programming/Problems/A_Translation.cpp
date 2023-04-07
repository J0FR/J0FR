// https://codeforces.com/problemset/problem/41/A

#include <bits/stdc++.h>
using namespace std;

int main() {
    string caso, comparar;
    cin >> caso >> comparar;
    reverse(caso.begin(), caso.end());
    
    if (comparar == caso) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }
}
