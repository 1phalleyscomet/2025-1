//예외 처리 구문
/*
try {
	throw 예외값 } catch(예외형식 예외이름){
	}
*/
#include <iostream>
using namespace std;

int main() {
	try {
		int input;
		cout << "정수 중 하나를 입력하세요:";
		cin >> input;

		if (input > 0) {
			cout << "throw 1" << endl;
			throw 1;
			cout << "after throw 1" << endl;
		}

		if (input < 0) {
			cout << "throw -1.0f" << endl;
			throw - 1.0f;
			cout << "after throw -1.0f" << endl;
		}

		if (input == 0) {
			cout << "throw Z" << endl;
			throw 'Z';
			cout << "after throw Z" << endl;
		}
	}

	catch (int a) {
		cout << "catch" << a << endl;
	}
	catch (float b) {
		cout << "catch" << b << endl;
	}
	catch (char c) {
		cout << "catch" << c << endl;
	}
	catch (...) {
		cout << "catch all" << endl; //처리되지 않은 나머지 예외 모두 받기
	}
	return 0;
}//catch없을 시 런타임 오류 발생

