#include <vector>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n, m;
    cin >> n >> m;
    int mi_l = 0, mi_r = 10000000000;
    for(int i=0; i<m; i++){
        int l, r;
        cin >> l >> r;
        mi_l = max(mi_l, l);
        mi_r = min(mi_r, r);
    }
    int ans;
    ans = max(0, mi_r - mi_l + 1);
    cout << ans << endl;
    return 0;
}