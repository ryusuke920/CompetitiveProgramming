#include<bits/stdc++.h>

using namespace std;

int main() {
    int p; cin >> p;
    vector<int> a(10);
    for (int i = 0; i < 10; i++) {
        int sum = 1;
        for (int j = 1; j <= i + 1; j++) {
            sum *= j;
        }
        a[i] = sum;
    }

    // sort(a.rbegin(), a.rend()); も可能
    reverse(a.begin(), a.end());

    int ans = 0, sum = 0;
    while (sum < p) {
        for (int i = 0; i < 10; i++) {
            if (sum + a[i] <= p) {
                sum += a[i];
                ans += 1;
                break;
            }
        }
    }

    cout << ans << endl;
}