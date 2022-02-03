#include<bits/stdc++.h>
using namespace std;
int main() {
    int n, x; cin >> n >> x;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            ans += a[i];
        } else {
            ans += a[i] - 1;
        }
    }
    if (ans <= x) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}