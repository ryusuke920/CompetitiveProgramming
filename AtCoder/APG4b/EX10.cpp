#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    int i = 0;
    cout << "A:";
    while (i < a) {
        cout << "]";
        i++;
    }
    cout << endl;

    i = 0;
    cout << "B:";
    while (i < b) {
        cout << "]";
        i++;
    }
    cout << endl;
}