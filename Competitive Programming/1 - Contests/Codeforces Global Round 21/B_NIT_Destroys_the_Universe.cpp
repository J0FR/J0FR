#include <iostream>
#include <vector>
using namespace std;

int main() {
    int test_cases, n, val;
    cin >> test_cases;

    for (int x = 0; x < test_cases; x++){
        cin >> n;
        vector<int> v;
        for (int i = 0; i < n; i++){
            cin >> val;
            v.push_back(val);
        }
        if (v.back() != 0){
            v.push_back(0);
        }
        int count_result = -1;
        for (auto _:v){
            if (_ == 0){
                count_result++;
            }
        }
        
        if (count_result + 1 == n){
            cout << 0 << endl;
        } else if (count_result == -1){
            cout << 1 << endl;
        } else {
            cout << 2 << endl;
        }
    }
    return 0;
}