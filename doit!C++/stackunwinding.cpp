#include <iostream>
using namespace std;

void func_throw() {
	cout << endl;
	cout << "func_throw() 함수 내부" << endl;
	cout << "throw-1" << endl;
	throw - 1;
	cout << "after func_throw-1" << endl;

}

void func_2() {
	cout << endl;
	cout << "func_2() 함수 내부" << endl;
	cout << "func_throw()" << endl;
	func_throw();
	cout << "after func_throw()" << endl;
}

void func_1() {
	cout << endl;
	cout << "func_1() 함수 내부" << endl;
	cout << "func_2() 호출" << endl;
	func_2();
	cout << "after func_2()" << endl;
}

int main() {
	cout << "main 내부" << endl;
	try {
		cout << "func_1() 호출" << endl;
		func_1();
	}
	catch (int exec) {
		cout << endl;
		cout << "catch" << exec << endl;
	}
	return 0;
}
//예외가 처리되지 않아 함수를 호출한 쪽으로 전달되는 현상 : 스택풀기