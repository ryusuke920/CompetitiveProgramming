#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> a(3);
    for (int i = 0; i < 3; i++) cin >> a[i];
    cout << *max_element(a.begin(), a.end()) - *min_element(a.begin(), a.end()) << endl;
}