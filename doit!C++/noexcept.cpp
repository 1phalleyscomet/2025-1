/*함수가 예외를 던지지 않음을 명시
int func() noexcept*/
/*함수가 예외를 던지는지 확인
bool does_not_throw=noexcept(my_function());*/

//noexcept함수에서 예외 던지기
#include <iostream>
using namespace std;

void real_noexcept() noexcept {
	cout << "real_noexcept" << endl;
}

void fake_noexcept() noexcept {
	cout << "fake_noexcept" << endl;
	throw 1;
}

int main() {
	real_noexcept();

	try {
		fake_noexcept();
	}
	catch (int exec) {
		cout << "catch" << exec << endl;
	}

	return 0;
}

//runtime error