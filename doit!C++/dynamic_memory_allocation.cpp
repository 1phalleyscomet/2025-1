/*고정크기 배열선언 예)
char char_array[10];
int int_array[500];
float float_array[1000];*/

//동적 메모리 할당
//자료형 *변수명 = new 자료형;

//동적 메모리 해제
//delete 변수명;

#include <iostream>
using namespace std;

int main() {
	int* pt_int_value = new int;

	*pt_int_value = 100;
	cout << *pt_int_value << endl;

	delete pt_int_value;

	//배열 형태의 동적 메모리 할당과 과제
	// 자료형 *변수명 = new 자료형[크기];
	// delete[] 변수명;

	int* pt_int_array_value = new int[5];
	
	for (int i = 0; i < 5; i++) {
		pt_int_array_value[i] = i; //할당된 배열 변수에 0-4 순서대로 넣기
	}

	for (int i = 0; i < 5; i++) {
		cout << pt_int_array_value[i] << endl; //배열 변수 출력
	}

	delete[] pt_int_array_value;

	/*동적 메모리 할당을 해제하는 이유
	일반변수->stack에 할당
	->함수 반환 시 자동 소멸
	
	동정할당변수->heap에 할당
	->명시적 해제 전 할당 상태 유지->메모리 누수, 메모리 과다 사용*/

	return 0;
}