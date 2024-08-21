#include<bits/stdc++.h>
using namespace std;

template <typename T> void chmin(T&x,const T &y)
{
	if(x>y)x=y;
}
template <typename T> void chmax(T &x,const T &y)
{
	if(x<y)x=y;
}
typedef long long s64;
typedef unsigned long long u64;
typedef unsigned int u32;
typedef pair<int,int> pii;
#define rep(i,l,r) for(int i=l;i<=r;++i)
#define per(i,r,l) for(int i=r;i>=l;--i)
#define rep0(i,l,r) for(int i=l;i<r;++i)
#define gc (c=getchar())
int read()
{
	char c;
	while(gc<'-');
	if(c=='-')
	{
		int x=gc-'0';
		while(gc>='0')x=x*10+c-'0';
		return -x;
	}
	int x=c-'0';
	while(gc>='0')x=x*10+c-'0';
	return x;
}
#undef gc

const int N=1e5+5;
char s[N];
int dp[N][4][4],dy[128];

int main()
{
#ifdef kcz
	freopen("1.in","r",stdin);//freopen("1.out","w",stdout);
#endif
	rep(i,0,3)
	rep(j,0,3)dp[0][i][j]=-1e9;
	dp[0][0][0]=0;
	dy['c']=0;dy['u']=1;dy['t']=2;dy['e']=3;
	int n;
	cin>>n;
	scanf("%s",s+1);
	rep(i,1,n)
	{
		int x=dy[s[i]];
		rep(a,0,3)
		rep(b,0,3)
		{
			dp[i][a][b]=dp[i-1][a][b];
			if((x+1)%4==a)chmax(dp[i][a][b],dp[i-1][x][b]+4*(a==0));
			if((3-x+1)%4==b)chmax(dp[i][a][b],dp[i-1][a][3-x]+4*(b==0));
		}
	}
	int ans=0;
	rep(i,0,3)
	rep(j,0,3)chmax(ans,dp[n][i][j]);
	cout<<ans;
}


//2nd
#include<bits/stdc++.h>
using namespace std;
int n,i,j,k,f[100005][4][4],a[300];
char c[100005];
int main()
{
	scanf("%d%s",&n,c+1);
	a['c']=0;
	a['u']=1;
	a['t']=2;
	a['e']=3;
	memset(f[0],128,sizeof(f[0]));
	f[0][0][0]=0;
	for(i=1;i<=n;i++)
	{
		for(j=0;j<4;j++)
		    for(k=0;k<4;k++)
		        f[i][j][k]=f[i-1][j][k];
		for(j=0;j<4;j++)
		{
			f[i][a[c[i]]+1&3][j]=max(f[i][a[c[i]]+1&3][j],f[i-1][a[c[i]]][j]+1);
			f[i][j][a[c[i]]]=max(f[i][j][a[c[i]]],f[i-1][j][a[c[i]]+1&3]+1);
		}
	}
	cout<<f[n][0][0]<<endl;
	return 0;
}
