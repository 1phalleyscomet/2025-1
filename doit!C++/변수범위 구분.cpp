#include <iostream>
using namespace std;

int value = 1;

int main() {
	int value = -1;
	cout << value << endl; //지역변수
	cout << ::value << endl; //전역변수

	return 0;
}
