#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, s; cin >> n >> s;
    vector<int> a(n);
    vector<int> p(n);
    for(int i = 0; i < n; i++) cin >> a[i];
    for(int i = 0; i < n; i++) cin >> p[i];
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (a[i] + p[j] == s) {
                ans += 1;
            }
        }
    }
    cout << ans << endl;
}
