#include <vector>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    const int n_max = 40, abmax = 10, INF=1000000;

    int a[n_max], b[n_max], c[n_max];
    int dp[n_max + 1][n_max * abmax + 1][n_max * abmax + 1];
    int n, ma, mb;
    cin >> n >> ma >> mb;

    for (int i=0;i<n;i++) {
        cin >> a[i] >> b[i] >> c[i];
    }

    for (int i=0;i<=n;i++) {
        for (int j=0;j<=n_max * abmax;j++) {
            for (int k=0;k<=n_max * abmax;k++) {
                dp[i][j][k] = INF;
            }
        }
    }

    dp[0][0][0] = 0;
    for (int i=0;i<n;i++) {
        for (int j=0;j<=n_max * abmax;j++) {
            for (int k=0;k<=n_max * abmax;k++) {
                if (dp[i][j][k] == INF) continue;
                dp[i + 1][j][k] = min(dp[i][j][k], dp[i + 1][j][k]);
                dp[i + 1][j + a[i]][k + b[i]] = min(dp[i + 1][j + a[i]][k + b[i]], dp[i][j][k] + c[i]);
            }
        }
    }

    int ans = INF;
    for (int i=1;i<=n_max * abmax;i++) {
        for (int j=1;j<=n_max * abmax;j++) {
            if (i * mb == j * ma) ans = min(ans, dp[n][i][j]);
        }
    }

    if (ans == INF) ans = -1;
    cout << ans << endl;

    return 0;
}