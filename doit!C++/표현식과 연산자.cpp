//전/후위 연산
#include <iostream>
using namespace std;

int main() {
	int a = 0;
	int b = 0;
	int a_prefix;
	int b_postfix;

	a_prefix = ++a; //전위연산 a값 1증가 후 대입
	b_postfix = b++; //후위연산 대입 후 b값 1 증가

	cout << "a= " << a << ", " << "a_prefix=" << a_prefix << endl;
	cout << "b=" << b << ", " << "b_postfix=" << b_postfix << endl;

	return 0;
}

/*logic NOT

0==false
!0==true*/

//bit operator
int sub() {
	unsigned int value = 0x00000000;

	value = ~value; // 비트열 반전
	cout << hex << value << endl;

	return 0;
}