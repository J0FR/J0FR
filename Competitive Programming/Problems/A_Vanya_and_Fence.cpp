// https://codeforces.com/problemset/problem/677/A


// Answer - Accepted

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, h, value, i, contador = 0;
    cin >> n >> h;

    for (i = 0; i < n; ++i){
        cin >> value;
        if (value <= h) {
            contador += 1;
        }
        else {
            contador += 2;
        }
    }
    cout << contador;
}


// Another answer - Not accepted

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, h, arr[100], i, contador = 0;
    cin >> n >> h;
    for (i = 0; i < n; ++i) {
        scanf("%d", &arr[i]);
    }

    for (i = 0; i < n; ++i){
        if (arr[i] <= h) {
            contador += 1;
        }
        else {
            contador += 2;
        }
    }
    cout << contador;
}