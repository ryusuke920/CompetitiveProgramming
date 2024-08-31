// g++ hoge.cpp -std=gnu++17 && ./a.out

#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define pb push_back
#define fs first
#define sc second
#define all(X) (X).begin(), (X).end()
#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define fore(i, a) for (auto &i : a)
template <class T > using v = vector<T>;
template <class T> using vv = v<v<T>>;
template <class T> using vvv = v<v<v<T>>>;
using vl = v<ll>;
using vvl = vv<ll>;
using vvvl = vvv<ll>;

bool comp(int i, int j) { return i > j; }
template<typename T> bool chmin(T &a, const T &b) { if (a > b) { a = b; return true; } return false; }
template<typename T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return true; } return false; }
template <typename T> istream &operator>>(istream &is, vector<T> &x) { for (auto &y : x) { is >> y; } return is; }
template <class T> ostream &operator<<(ostream &os, vector<T> &x) { for (unsigned int i = 0, size = x.size(); i < size; i++) os << x[i] << (i == size - 1 ? "" : " "); return os; }
template <class T, class S> istream &operator>>(istream &is, pair<T, S> &x) { is >> x.first >> x.second; return is; }
template <class T, class S> ostream &operator<<(ostream &os, pair<T, S> &x) { os << x.first << " " << x.second; return os; }


int main() {
    ll H, W, N;
    cin >> H >> W >> N;
    v<pair<ll, ll>> v(N);
    vvl h(H);
    rep(i, N) {
        cin >> v[i];
        v[i].fs--;
        v[i].sc--;
        h[v[i].fs].pb(v[i].sc);
    }
    fore(i, h) {
        sort(all(i));
    }

    map<ll, pair<ll, pair<ll, ll>>> dp;
    dp[-1] = {0, {-1, -1}};
    dp[1000000000000000000LL] = {1000000000000000000LL, {1000000000000000000LL, 1000000000000000000LL}};
    map<pair<ll, ll>, pair<ll, ll>> parents;

    auto dp1 = [&](ll index_, ll value, ll x, ll y) {
        while (true) {
            auto iter = dp.lower_bound(index_);
            if (iter->second.fs <= value) {
                dp.erase(iter);
            } else {
                break;
            }
        }
        dp[index_] = {value, {x, y}};
    };

    rep(i, H) {
        fore(index_, h[i]) {
            auto iter = dp.upper_bound(index_);
            iter--;
            ll value = iter->second.fs;
            parents[{i, index_}] = iter->second.sc;
            dp1(index_, value + 1, i, index_);
        }
    }

    // auto iter = dp.upper_bound(1000000000000000000LL);
    auto iter = dp.lower_bound(1000000000000000000LL);
    iter--;

    // pair[1]の[0]
    cout << iter->second.fs << endl;

    vector<pair<ll, ll>> ans;
    auto num = iter->second.sc;
    ans.pb({H - 1, W - 1});
    // 復元
    while (num != pair<ll, ll>(-1, -1)) {
        ans.pb(num);
        num = parents[num];
    }
    ans.pb({0, 0});
    reverse(all(ans));

    string ans_str = "";
    rep(i, ans.size() - 1) {
        ans_str += string(ans[i + 1].fs - ans[i].fs, 'D') + string(ans[i + 1].sc - ans[i].sc, 'R');
    }
    
    cout << ans_str << endl;

    return 0;
}
