//static 자동지속->정적지속 변수 유효 범위 변경
// 지역변수->정적변수 전환

#include <iostream>
using namespace std;

void func() {
	int a = 10;
	static int b = 10;

	a++;
	b++;

	cout << "a:" << a << ",b:" << b << endl;

}

int main() {

	func();
	func();
	func();
	func();
	func();

	return 0;
}

/*지역변수 a->func함수 호출 시 새로 생성, 종료 시 소멸
b-> 정적변수 func함수 호출 만큼 값 누적 *반드시 초기화* */

int getNewID() {
	static int ID = 0;
	return ++ID;
}

int main() {
	cout << "ID:" << getNewID() << endl;
	cout << "ID:" << getNewID() << endl;
	cout << "ID:" << getNewID() << endl;
	cout << "ID:" << getNewID() << endl;

	return 0;
}

/*지역변수 ->stack 영역 저장
정적변수->data 영역 저장(프로그램 시작 시 할당, 종료 시 해제)*/

