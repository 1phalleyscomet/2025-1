//const 변수 상수화
//초기화 필수

#include <iostream>
using namespace std;

int main() {
	const int a = 1;
	a = 2;  //컴파일 오류 발생

	return 0;
}

//포인터 변수 상수화

int main() {
	int a = 0;
	const int* ptr = &a; //*ptr 상수화
	a = 1; //컴파일 통과
	*ptr = 2; //컴파일 에러

	return 0;
}

int main() {
	int a = 0;
	int b = 1;
	int* const ptr = &a; //ptr을 상수화
	a = 1;
	ptr = &b; //컴파일 에러

	return 0;
}

//*ptr 상수화=포인터 변수가 가리키는 값을 상수화
//ptr상수화=포인터 변수 자체를 상수화
//const 사용 시 해당 값 변경 X