#include<bits/stdc++.h>
using namespace std;

#define pb push_back
#define fs first
#define sc second

using ll = long long;
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

bool f(tuple<ll, ll, ll> l, tuple<ll, ll, ll> r){
	auto [x1, y1, z1] = l;
	auto [x2, y2, z2] = r;
	ll lx = x1 * (x2 + y2);
	ll rx = x2 * (x1 + y1);
	if (lx != rx) return lx > rx;
	return z1 < z2;
}


int main(){
	ll n;

	vector<tuple<ll,ll,ll>> vp;
	cin >> n;
	vp = vector<tuple<ll, ll, ll>>(n);
	int ind = 1;
	for(auto &[i, j, k]:vp){
		cin >> i >> j;
		k = ind++;
	}

	sort(vp.begin(), vp.end(), f);
	for(auto &[i, j, k]: vp){
		cout << k << ' ';
	}
	cout << endl;

}
