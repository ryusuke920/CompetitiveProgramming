// g++ -o hoge hoge.cpp -std=c++14
// https://teratail.com/questions/263523
// g++ main.cpp -std=gnu++17 && ./a.out
// -o も端折ると一気に && で実行できる

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
template <class T> using v = vector<T>;
template <class T> using vv = v<v<T>>;
template <class T> using vvv = v<vv<T>>;
using vl = v<ll>;
using vvl = vv<ll>;
using vvvl = vvv<ll>;

// next_permutation で使ったやつ
bool comp(int i, int j) {
    return i > j;
}

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
template <class T>
ostream &operator<<(ostream &os, vector<T> &x) {
  for (unsigned int i = 0, size = x.size(); i < size; i++)
    os << x[i] << (i == size - 1 ? "" : " ");
  return os;
}
template <class T, class S>
istream &operator>>(istream &is, pair<T, S> &x) {
  is >> x.first >> x.second;
  return is;
}
template <class T, class S>
ostream &operator<<(ostream &os, pair<T, S> &x) {
  os << x.first << " " << x.second;
  return os;
}

int main() {
    ll n;
    cin >> n;
    vl a(3 * n);
    cin >> a;

    vl cnt(n, 0);
    vector<vector<int>> f(n, vector<int>(2, 0));
    rep(i, n) f[i][0] = i + 1;

    rep(i, 3 * n) {
        cnt[a[i] - 1] += 1;
        if (cnt[a[i] - 1] == 2) {
            f[a[i] - 1][1] = i + 1;
        }
    }

    sort(f.begin(), f.end(), [](const vector<int>& x, const vector<int>& y) {
        return x[1] < y[1];
    });

    vl ans;
    rep(i, n) ans.pb(f[i][0]);

    rep(i, n) cout << ans[i] << " ";
    cout << endl;

    return 0;
}