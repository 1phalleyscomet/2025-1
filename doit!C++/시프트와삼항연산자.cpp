#include <iostream>
#include <bitset>

using namespace std;

int main() {
	int a = 13;
	int b = a >> 1;
	int c = a << 1;

//int d = a >> -1; ����Ʈ ���� ����
//int e = a << 32; ����Ʈ ���� ����

cout << "a=" << bitset<8>(a) << ":" << a << endl;
cout << "b=" << bitset<8>(b) << ":" << b << endl;
cout << "c=" << bitset<8>(c) << ":" << c << endl;


