#include <vector>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main(){
    int a, b, c;
    cin >> a >> b >> c;
    int ans = 0;
    ans = max(abs(a - b), abs(a - c));
    ans = max(ans, abs(b - c));
    cout << ans << endl;
    return 0;
}