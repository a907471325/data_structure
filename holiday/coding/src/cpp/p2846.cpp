#include<iostream>
using namespace std;

const int N = 100010;
typedef long long ll;

ll tree[N * 4];
bool lazy[N * 4];

int a[N];
#define lson ((root<<1))
#define rson ((root<<1)+1)
#define mid (l+r>>1)

void fun(int root, int l, int r) {
	tree[root] = (r - l + 1) - tree[root];
	lazy[root] = !lazy[root];
}
void pushdown(int root, int l, int r) {
	if (lazy[root]) {
		fun(lson, l, mid);
		fun(rson, mid + 1, r);
		lazy[root] = false;
	}
	
}
void update(int root, int l, int r, int lr, int rr) {
	if (r < lr || rr < l) {
		return;
	}
	if (lr <= l && r <= rr) {
		fun(root, l, r);
		return;
	}
	pushdown(root, l, r);
	update(lson, l, mid, lr, rr);
	update(rson, mid + 1, r, lr, rr);
	tree[root] = tree[lson] + tree[rson];
}
ll query(int root, int l, int r, int lr, int rr) {
	if (r < lr || rr < l) {
		return 0;
	}
	if (lr <= l && r <= rr) {
		return tree[root];
	}
	pushdown(root, l, r);
	return (ll)query(lson, l, mid, lr, rr) + (ll)query(rson, mid + 1, r, lr, rr);
}

int n, m;
int main() {

	cin >> n >> m;
	for (int a, b, c, i = 1;i <= m;i++) {
		cin >> a;
		if (a == 0) {
			cin >> b >> c;
			update(1, 1, n, b, c);
		}
		else {
			cin >> b >> c;
			cout << (ll)query(1, 1, n, b, c) << endl;
		}		

	}
}