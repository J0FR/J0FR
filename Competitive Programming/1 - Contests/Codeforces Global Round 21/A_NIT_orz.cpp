#include <iostream>
#include <vector>
using namespace std;

int main() {
    int test_cases, n, z, val, max;
    cin >> test_cases;

    for (int x = 0; x < test_cases; x++){
        max = 0;
        cin >> n >> z;
        vector<int> v;

        for (int i = 0; i < n; i++){
            cin >> val;
            v.push_back(val);
        }

        for (auto _:v){
            int or_answer = _ | z;
            int and_answer = _ & z;
            if (or_answer > max){
                max = or_answer;
            } else if (and_answer > max){
                max = and_answer;
            }  
        }
        cout << max << endl; 
    }
    return 0;
}