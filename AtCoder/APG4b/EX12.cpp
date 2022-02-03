#include <bits/stdc++.h>
using namespace std;

int main() {
    string s; cin >> s;
    int cnt_plus = 0, cnt_minus = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s.at(i) == '+') {
            cnt_plus++;
        }
        else if (s.at(i) == '-') {
            cnt_minus++;
        }
    }
    cout << 1 + cnt_plus - cnt_minus << endl;
}