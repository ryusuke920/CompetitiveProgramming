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
using Pair = pair<int, int>;

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

void is_ok(int dx, int dy, vector<string> &matrix, vector<vector<int>> &num) {
    rep(i, 4) {
        rep(j, 4) {
            // rep(k, 4) {

            // }
            int x = dx + i;
            int y = dy + j;
            if (matrix[i][j] == '#') {
                if (0 <= x && x < 4 && y >= 0 && y < 4) {
                    num[x][y]++;
                } else {
                    num[0][0] += 1e8;
                }
            }
        }
    }
}

void check(vector<string> &matrix) {
    vector<string> temp(4, string(4, ' '));
    rep(i, 4) {
        rep(j, 4) {
            temp[j][4 - i - 1] = matrix[i][j];
        }
    }
    matrix = temp;
}

void solve(const vector<vector<string>> &poly) {
    vector<Pair> shifts;
    for (int i = -3; i <= 3; i++) {
        for (int j = -3; j <= 3; j++) {
            shifts.emplace_back(i, j);
        }
    }
    rep(i, 4) {
        rep(j, 4) {
            rep(k, 4) {
                vector<vector<string>> pp = poly;
                rep(_, i) check(pp[0]);
                rep(_, j) check(pp[1]);
                rep(_, k) check(pp[2]);
                for (int i2 = 0; i2 < shifts.size(); i2++) {
                    for (int j2 = 0; j2 < shifts.size(); j2++) {
                        for (int k2 = 0; k2 < shifts.size(); k2++) {
                            vector<vector<int>> num(4, vector<int>(4, 0));
                            is_ok(shifts[i2].first, shifts[i2].second, pp[0], num);
                            is_ok(shifts[j2].first, shifts[j2].second, pp[1], num);
                            is_ok(shifts[k2].first, shifts[k2].second, pp[2], num);
                            bool ok = true;
                            rep(x, 4) {
                                rep(y, 4) {
                                    if (num[x][y] != 1) {
                                        ok = false;
                                    }
                                }
                            }
                            if (ok) {
                                cout << "Yes" << endl;
                                return;
                            }
                        }
                    }
                }
            }
        }
    }
    cout << "No" << endl;
    return;
}

int main() {
    vector<vector<string>> poly(3, vector<string>(4));
    for (auto &matrix : poly) {
        for (auto &i : matrix) {
            cin >> i;
        }
    }
    
    solve(poly);

    return 0;
}
