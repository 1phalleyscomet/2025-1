//변수에 또 다른 별칭을 부여함
//매개변수를 일반 변수로 선언
#include <iostream>
using namespace std;

void swap(int a, int b) {
	//swap함수 내 교환 전 a,b값

	cout << "[swap func] before swap, a: " << a << "b:" << b << endl;

	int temp = a;
	a = b;
	b = temp;

	//swap함수 내 교환 후 a,b값
	cout << "[swap func] after swap, a: " << a << "b:" << b << endl;

}

int main() {
	int a = 5;
	int b = 10;

	//swap함수 호출 전 a,b값
	cout << "[main] before swap, a: " << a << "b:" << b << endl;
	swap(a, b);

	//swap함수 호출 후 a,b값
	cout << "[main] after swap, a: " << a << "b:" << b << endl;

	return 0;
}

//swap 매개변수로 받은 두 정수 교환 함수
//값에 의한 호출(call by value) 값을 전달하는 호출 방식, 값이 매개변수로 복사->새로운 변수(main함수 변숫값 변화X)

/*레퍼런스 변수 선언
* 자료형 &레퍼런스 변수 이름=대상 변수 이름; */

//레퍼런스 변수 선언
void swap(int& ref_a, int& ref_b) {
	cout << "[swap func] before swap, ref_a: " << ref_a << "ref_b:" << ref_b << endl;

	int temp = ref_a;
	ref_a = ref_b;
	ref_b = temp;
	cout << "[swap func] after swap, ref_a: " << ref_a << "ref_b:" << ref_b << endl;


}

int main() {
	int a = 5;
	int b = 10;

	cout << "[main] before swap, a: " << a << "ref_b:" << b << endl;

	swap(a, b);

	//swap함수 호출 후 a,b값
	cout << "[main] after swap, a: " << a << "b:" << b << endl;

	return 0;
}

//실제 변수 a,b->ref_a,ref_b 별칭 획득
//참조에 의한 호출(call by reference) 피호출자(main)변수 그대로 이용
//반드시 원본 변수 지정
//지정 변수 대상 변경 불가
//상수 참조 불가