#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
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


ll N;
vector<ll> A;
map<ll,ll> mp;
ll op(ll a,ll b) {
    return a + b;
}

ll e() {
    return 0;
}

segtree<ll, op, e> seg1, seg2;


int main() {
    cin >> N;
    A.resize(N);
    rep(i, N) cin >> A[i];

    seg1 = segtree<ll, op, e>(N);
    seg2 = segtree<ll, op, e>(N);

    ll ans = 0;
    ll num = 0;
    set<ll> set_;
    for(auto i: A) set_.insert(i);
    ll cnt = 0;

    for(auto i: set_){
        mp[i] = cnt;
        cnt += 1;
    }

    rep(i, N) {
        ans += seg1.prod(0, mp[A[i]]) - A[i] * seg2.prod(0, mp[A[i]]);
        // ans += seg1.prod(0, mp[A[i] - 1]) - A[i] + seg2.prod(0, mp[A[i]]);
        {
            ll x = seg1.get(mp[A[i]]);
            // ll x = seg1.get(mp[A[i] - 1]);
            seg1.set(mp[A[i]], x + A[i]);
            
            ll cnt = seg2.get(mp[A[i]]);
            seg2.set(mp[A[i]], cnt + 1);
        }
    }

    cout << -ans << endl;

    return 0;
}