#include<iostream>
using namespace std;

const int N = 100010;
typedef long long ll;

ll tree[N * 4];
ll lazy[N * 4];

int a[N];
#define lson ((root<<1))
#define rson ((root<<1)+1)
#define mid (l+r>>1)

void build(int root, int l, int r) {// O(n) 建树
	if (l == r) {
		tree[root] = a[l];//如果递归到了最底层，直接返回。
		return;
	}
	build(lson, l, mid);//分别递归左右子树。
	build(rson, mid + 1, r);
	tree[root] = tree[lson] + tree[rson];//重新计算这个节点所覆盖的元素的和。
}

void fun(int root, int l, int r, int v) {//推标记
	tree[root] += (r - l + 1) * v;
	lazy[root] += v;
}
void pushdown(int root, int l, int r) {//放标记
	fun(lson, l, mid, lazy[root]);
	fun(rson, mid + 1, r, lazy[root]);
	lazy[root] = 0;
}
void update(int root, int l, int r, int lr, int rr, int v) {//更新
	if (r < lr || rr < l) {//如果现在这个节点所代表的线段完全不在更新的范围之内，直接返回。
		return;
	}
	if (lr <= l && r <= rr) {//如果现在这个节点所代表的线段完全在更新的范围之内，直接推标记。
		fun(root, l, r, v);
		return;
	}
	pushdown(root, l, r);//下放标记。
	update(lson, l, mid, lr, rr, v);
	update(rson, mid + 1, r, lr, rr, v);
	tree[root] = tree[lson] + tree[rson];//重新计算这个节点所覆盖的元素的和。
}
ll query(int root, int l, int r, int lr, int rr) {//差不多和update函数一样。
	if (r < lr || rr < l) {//如果现在这个节点所代表的线段完全不在查询的范围之内，直接返回。
		return 0;
	}
	if (lr <= l && r <= rr) {//如果现在这个节点所代表的线段完全在查询的范围之内，直接sum。
		return tree[root];
	}
	pushdown(root, l, r);//下放标记
	return (ll)query(lson, l, mid, lr, rr) + (ll)query(rson, mid + 1, r, lr, rr);
}
int n, m;
int main() {
	
	cin >> n >> m;
	for (int i = 1;i <= n;i++) {
		cin >> a[i];
	}
	build(1, 1, n);
	for (int a, b, c, d, i = 1;i <= m;i++) {
		cin >> a;
		if (a == 1) {
			cin >> b >> c >> d;
			update(1, 1, n, b, c, d);
		}
		else {
			cin >> b >> c;
			cout << (ll)query(1, 1, n, b, c) << endl;
		}
	}
}