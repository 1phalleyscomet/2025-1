#include <iostream>
#include <string>
using namespace std;

int main() {
	int customer_num = 0;

	cout << "방문 손님:";
	cin >> customer_num; //손님 수 입력

	string* bread = new string[customer_num]; //손님 수 만큼 string 배열 생성

	for (int i = 0; i < customer_num; i++) {
		bread[i] = "빵_" + to_string(i); //빵_숫자 형태로 배열에 저장 //to_string() 숫자를 문자열로 변환하는 함수

	}

	cout << endl << "--생산된 빵--" << endl;
	for (int i = 0; i < customer_num; i++) {
		cout << *(bread + i) << endl;
	}

	delete[] bread;

	return 0;

}

/* 포인터 역참조 전 포인터가 유효한 메모리를 가리키는지 확인->segmentation fault, runtime error 발생
할당된 메모리 범위를 벗어나는 포인터 연산 X
할당 헤제된 메모리 역참조 X */