#include<bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    vector<long long> c(n);
    int mod = 1000000007;
    for (int i = 0; i < n; i++) cin >> c[i];
    sort(c.begin(), c.end());
    int ans = 1;
    for (int i = 0; i < n; i++) ans = ans * max(0LL, c[i] - i) % mod;
    cout << ans << endl;
}