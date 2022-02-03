#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> data(5);
  for (int i = 0; i < 5; i++) cin >> data[i];
  int x = 1;
  for (int i = 0; i < 4; i++) {
      if (data[i] == data[i + 1]) {
          cout << "YES" << endl;
          x = 0;
          break;
      }
  }

  if (x == 1) {
      cout << "NO" << endl;
  }

}
