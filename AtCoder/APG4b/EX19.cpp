#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<vector<int> > ans(9, vector<int>(9));
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            ans[i][j] = (i + 1) * (j + 1);
        }
    }

    vector<vector<int> > a(9, vector<int>(9));
    for (int i = 0; i < 9; i ++) {
        for (int j = 0; j < 9; j++) {
            cin >> a[i][j];
        }
    }

    int correct = 0, wrong = 0;

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (ans[i][j] != a[i][j]) {
                wrong += 1;
            } else {
                correct += 1;
            }
        }
    }

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cout << ans[i][j];
            if (j < 8) {
                cout << ' ';
            } else {
                cout << endl;
            }
        }
    }

    cout << correct << endl;
    cout << wrong << endl;
}