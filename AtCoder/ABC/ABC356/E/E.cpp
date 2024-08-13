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
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll N;
    cin >> N;
    vl A(N);
    cin >> A;

    sort(A.rbegin(), A.rend());
    // vl B(N, 0);
    ll inf = 10101050;
    vl sum_(inf);
    ll ans = 0;
    // rep(i, N) {
    //     t = (t + get(a[i]));
    //     ans = ans + t * a[i] % m + sum_[i+1];
    //     
    // }
    rep(i, N) {
        const ll sqrt_ = 1030;
        for (ll k = 1; k < sqrt_ + 1; k++) {
            sum_[sqrt_] += 1;
            ll p = A[i] / k + 1;
            if (p < sqrt_) p = sqrt_;
            sum_[p] -= 1;
        }
        for (ll k = 1; k < sqrt_; k++) {
            sum_[k] += A[i] / k;
            sum_[k + 1] -= A[i] / k;
        }
        // for (ll k = 1; k < j; k++) {
        //     sum_[k] += (A[i] + 1) / k;
        //     sum_[k + 1] -= (A[i] + 1) / k;
        // }
    }


    // 累積和
    for (ll i = 1; i < inf; i++) {
        sum_[i] += sum_[i - 1];
    }
    // 総和を求めてほうじょ
    rep(i, N) {
        ans += sum_[A[i]] - 1;
    }

    map<ll, ll> s;
    rep(i, N) {
        s[A[i]] += 1;
    }

    for (auto &i: s) {
        ans -= i.sc*(i.sc - 1) / 2;
    }

    cout << ans << endl;

    return 0;
}