#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];
  int sum = 0;
  for (int i = 0; i < n; i++) {
      sum += a[i];
  }
  sum /= n;
  for (int i = 0; i < n; i++) {
      cout << abs(a[i] - sum) << endl;
  }
}