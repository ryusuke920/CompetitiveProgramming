#include "bits/stdc++.h"
using namespace std;
using ll=int64_t;

int main(){
	int n, W;
	cin >> n >> W;
	vector<ll>v(n), w(n);
	for(int i = 0; i<n; i++) cin >> v[i] >> w[i];
	vector<vector<ll> >dp(n + 1, vector<ll>(W + 1));

	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= W; j++) {
			if (j >= w[i]) {
				dp[i + 1][j] = max(dp[i][j - w[i]] + v[i], dp[i][j]);
			}
			else dp[i + 1][j] = dp[i][j];
		}
	}
	cout << dp[n][W] << endl;
}