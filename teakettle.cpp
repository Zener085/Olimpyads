#include <iostream>
using namespace std;

int main() {
	int n, a, x, m;
	cin >> n;
	cin >> a;
	cin >> x;
	cin >> m;
	int water = n * a - x;
	int count = 0;
	do {
	    water -= m;
	    count++;
	} while (water >= m);
	
	cout << count;
	
	return 0;
}
