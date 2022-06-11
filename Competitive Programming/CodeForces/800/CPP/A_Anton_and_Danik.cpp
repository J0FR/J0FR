// https://codeforces.com/problemset/problem/116/A

#include <bits/stdc++.h>
using namespace std;

int main() {
    int games, i;
    int count_a = 0, count_b = 0;
    string cases;
    cin >> games >> cases;

    for (i = 0; i < games; i++) {
        if (cases[i] == 'A') {
            count_a += 1;
        }
        else {
            count_b += 1;
        }
    }

    if (count_a > count_b) {
        cout << "Anton";
    }
    else if (count_a < count_b) {
        cout << "Danik";
    }
    else {
        cout << "Friendship";
    }
}