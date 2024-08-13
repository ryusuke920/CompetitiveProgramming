#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using ll = long long;
#define pb push_back
#define fs first
#define sc second
#define all(X) (X).begin(), (X).end()
#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define fore(i, n) for (auto &i : a)
 
bool comp(int i, int j) {
    return i > j;
}

template <class T> using v = vector<T>;
template <class T> using vv = v<v<T>>;
template <class T> using vvv = v<vv<T>>;
 
template<typename T>
bool chmin(T &a, const T &b) {
    if (a > b) {
        a = b;
        return true;
    }
    return false;
}
 
template<typename T>
bool chmax(T &a, const T &b) {
    if (a < b) {
        a = b;
        return true;
    }
    return false;
}
 
template <typename T> istream &operator>>(istream &is, vector<T> &x) {
  for (auto &y : x) {
    is >> y;
  }
  return is;
}



int main(){
    int n, m;
    vector<int> a, b;
    cin >> n >> m;
    a.resize(m);
    b.resize(m);

    for(int i = 0; i < m; i++) {
        cin >> a[i] >> b[i];
    }

    dsu uf(n);
    for(int i = 0; i < m; i++) {
        uf.merge(a[i] - 1, b[i] - 1);
    }
    ll ans = 0;
    for(auto &i: uf.groups()) {
        ans += (ll)i.size() * (i.size() - 1) / 2;
    }
    // cout << ans << endl;

    ans -= m;
    cout << ans << endl;

    return 0;
}