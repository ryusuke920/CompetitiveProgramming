#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    int a; cin >> a;
    for (int i = 0; i < n; i++) {
        int x;
        string op;
        cin >> op >> x;

        if (op == "+") {
            a += x;
        } else if (op == "-") {
            a -= x;
        } else if (op == "*") {
            a *= x;
        } else if (op == "/" && x != 0) {
            a /= x;
        } else {
            cout << "error" << endl;
            break;
        }

        cout << i + 1 << ":" << a << endl;
    }

}