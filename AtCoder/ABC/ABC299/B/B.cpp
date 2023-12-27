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
    int n, t;
    cin >> n >> t;
    vl c(n), r(n);
    cin >> c;
    cin >> r;
    int cnt = count(c.begin(), c.end(), t);

    int idx = 1, val = 0;
    if (cnt >= 1) {
        rep(i, n) {
            if (val < r[i] && t == c[i]) {
                val = r[i];
                idx = i + 1;
            }
        }
    } else {
        rep(i, n) {
            if (c[i] == c[0] && val < r[i]) {
                val = r[i];
                idx = i + 1;
            }
        }
    }

    cout << idx << endl;

    return 0;
}