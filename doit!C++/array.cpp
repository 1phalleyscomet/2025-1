//배열 선언
/*자료형 배열이름[크기]={값1,값2,...,값n};*/
//고정 배열
#include <iostream>
using namespace std;

int main() {
	int lotto[45] = { 1,2,3,...,45 };

	cout << "Today's Lotto:" << lotto[1] << "," << lotto[7] << "," << lotto[14] << "," << lotto[27] << endl;

	//배열 원소의 메모리 주소 확인하기
	cout << "lotto[0] address:" << &lotto[0] << endl;
	cout << "lotto[1] address:" << &lotto[1] << endl;
	cout << "lotto[2] address:" << &lotto[2] << endl;

	//배열 원소의 주소와 포인터 연산의 결과 비교
	cout << "(lotto+0) address:" << lotto + 0 << endl; //포인터 연산으로 배열 원소에 접근
	cout << "(lotto+1) address:" << lotto + 1 << endl;
	cout << "(lotto+2) address:" << lotto + 2 << endl;

	/*
	&lloto[0] == lotto + 0
	&배열변수[인덱스] == 배열변수+인덱스

	lotto->첫번째 원소 주소 &lotto[0] 가리킴
	*/

	//배열과 포인터 차이
	int array[5] = { 1,2,3,4,5 };
	int* pointer_array = array;

	cout << "array: " << array << endl;
	cout << "pointer_array: " << pointer_array << endl << endl;

	cout << "sizeof(array): " << sizeof(array) << endl;
	cout << "sizeof(pointer_array) : " << sizeof(pointer_array) << endl;
	//배열 전체 크기 20byte
	//포인터 고정 크기 8byte

	//포인터 연산으로 수행
	cout << "Today's Lotto:" << *lotto << "," << *(lotto + 7) << "," << *(lotto + 14) << "," << *(lotto + 27) << endl;


	return 0;
}