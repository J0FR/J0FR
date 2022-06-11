// https://codeforces.com/problemset/problem/271/A

#include <bits/stdc++.h>
using namespace std;

bool all_different_numbers(int number) {
    int i;
    string str_number;
    str_number = to_string(number);
    for (i = 0; i < str_number.size(); i++) {
        char character = str_number[i];
        if (count(str_number.begin(), str_number.end(), character) > 1) {
            return false;
        }
    }
    return true;
}

int main() {
    int year;
    bool flag;
    cin >> year;
    year += 1;
    flag = all_different_numbers(year);
    while (flag != true) {
        year += 1;
        flag = all_different_numbers(year);
    }
    cout << year;
}

