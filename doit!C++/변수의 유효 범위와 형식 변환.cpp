//지역범위
#include <iostream>
using namespace std;

void print() {
	int value = 10;
	cout << "print 함수 내부에서의 지역변수 value:" << value << endl;
}

int main() {
	int value = 5;
	cout << "main함수 내부에서의 지역변수 value:" << value << endl;
	//함수명(value)이 동일하나 영향받지 않음
	print(); //print함수 호출
	cout << "다시 main 함수 내부에서의 지역변수 value:" << value << endl;

	return 0;
}
