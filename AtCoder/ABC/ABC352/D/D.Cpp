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
using p = pair<ll,ll>;
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

    ll N, K;
    vector<ll> P;
    cin >> N >> K;
    P = vl(N);

    rep(i, N) {
        cin >> P[i];
    }

    vector<p> A;
    rep(i, N) {
        A.pb({P[i], i});
    }

    sort(A.begin(), A.end());

    // cout << A << endl;
    set<ll> s;
    rep(i, K) {
        s.insert(A[i].sc);
    }
    // cout << s << endl;

    ll ans = *s.rbegin() - *s.begin();
    // ll ans = *s.begin() - *s.begin();
    // cout << ans << endl;

    rep(i, N - K) {
        s.erase(A[i].sc);
        s.insert(A[i + K].sc);
        ans = min(ans, *s.rbegin() - *s.begin());
    }
    
    cout << ans << endl;

    return 0;
}