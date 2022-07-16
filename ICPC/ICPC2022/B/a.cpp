#include<bits/stdc++.h>
using namespace std;
#include<atcoder/all>
using namespace atcoder;
using ll = long long;
int n,k;
deque<int> s,t;
const int MAX = 505050;
using mint = modint998244353;
mint fac[MAX],facinv[MAX];

void init(){
	fac[0] = fac[1] = 1;
	facinv[0] = facinv[1] = 1;
	for(int i = 2;i<MAX;i++){
		fac[i] = fac[i-1] * i;
		facinv[i] = fac[i].inv();
	}
}

mint biom(int n,int k){
	if(n<k)return 0;
	return fac[n] * facinv[n-k] * facinv[k];
}

void solve(){
	deque<deque<int>> vvi;
	map<int,int> t_idx;
	for(int i = 0;i<n;i++){
		t_idx[t[i]] = i;
	}
	{
		deque<int> add;
		int mxidx;
		for(int i = 0;i<n;i++){
			if(add.empty()){
				add.push_back(s[i]);
				mxidx = t_idx[s[i]];
			}
			else{
				if(mxidx<t_idx[s[i]]){
					mxidx = t_idx[s[i]];
					add.push_back(s[i]);
				}else{
					vvi.push_back(add);
					add.clear();
					add.push_back(s[i]);
					mxidx = t_idx[s[i]];
				}
			}
		}
		if(add.size()){
			vvi.push_back(add);
		}
	}
	cerr<<endl;
	for(auto &i:vvi){
		for(auto &j:i)cerr<<j<<' ';
		cerr<<endl;
	}
	{
		auto tmp = vvi;
		deque<int> chk;
		while(chk.size()<n){
			//for(auto &i:chk)cerr<<i<<' ';cerr<<endl;
			int mn = -1;
			for(int i = 0;i<vvi.size();i++){
				if(vvi.size()){
					if(mn==-1){
						mn = i;
					}else{
						if(vvi[mn].front()>vvi[i].front()){
							mn = i;
						}
					}
				}
			}
			chk.push_back(vvi[mn].front());
			vvi[mn].pop_front();
		}
		if(chk!=t){
			for(auto &i:chk)cerr<<i<<' ';cerr<<endl;
			for(auto &i:t)cerr<<i<<' ';cerr<<endl;
			cerr<<"!="<<endl;
			cout<<0<<endl;
			return;
		}
		vvi = tmp;
	}
	{
		int cnt = 0;
		for(int i = 0;i<vvi.size();i++){
			for(int j = 0;j<vvi[i].size()-1;j++){
				if(vvi[i][j]<vvi[i][j+1])cnt++;
			}
		}
		mint ans = 0;
		int nowgate = vvi.size();
		for(int i = nowgate;i<=k;i++){
			ans += biom(cnt,i-nowgate);
		}
		cout<<ans.val()<<endl;
	}

}

signed main(){
	cin.tie(nullptr);
	ios::sync_with_stdio(false);
	init();
	while(1){
		cin >> n >> k;
		if(n==0&&k==0)break;
		s = deque<int>(n);
		t = deque<int>(n);
		for(auto &i:s)cin >> i ;
		for(auto &i:t)cin >> i ;
		for(auto &i:s)i--;
		for(auto &i:t)i-- ;
		solve();
	}
}
