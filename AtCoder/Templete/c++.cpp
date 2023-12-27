#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using uint = unsigned int;

#define pb push_back
#define fs first
#define sc second
#define all(X) (X).begin(), (X).end()
#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define fore(i, n) for (auto &i : a)

int main() {
    int n;
    cin >> n;
    vector<int> h(n);
    rep(i, n) cin >> h[i];
    
    int ans = 0, height = 0;
    rep(i, n) {
        if (h[i] > height) {
            ans = i + 1;
            height = h[i];
        }
    }

    cout << ans << endl;

    return 0;
}