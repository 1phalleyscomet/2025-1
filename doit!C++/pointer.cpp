
//일반 변수 선언
#include <iostream>
using namespace std;

int main(){
	char char_value = 'A'; //1byte
	int int_value = 123; //4byte
	double double_value = 123.456; //8byte
//시작 메모리 주소 매 프로그램 실행 시 변경됨

	/*포인터 변수 선언
자료형 *(포인터 변수 이름);*/
//포인터-> 메모리 주소 저장 변수
	char* char_pointer_value = &char_value;
	int* int_pointer_value = &int_value;
	double* double_pointer_value = &double_value;
	//& 피연산자 주소 읽어오는 주소 연산자
	//포인터 변수 크기 != 데이터 형식
/*포인터 변수 선언 시 데이터 형식 지정-> 해당 포인터가 가리키는 데이터 형식 명시
->포인터 대상 연산 시 필요
->데이터 형식 일관성 유지
->오류 방지*/

	//일반 변수 데이터 출력
	cout << "char_value:" << char_value << endl;
	cout << "int_value:" << int_value << endl;
	cout << "double_value:" << double_value << endl;
	cout << endl; //줄바꿈

	//역참조 연산자*로 포인터 변수가 가리키는 데이터 출력
	cout << "*char_pointer_value:" << *char_pointer_value << endl;
	cout << "*int_pointer_value:" << *int_pointer_value << endl;
	cout << "*double_pointer_value:" << *double_pointer_value << endl;
	cout << endl;

	//역참조 연산자로 원본 데이터 덮어쓰기
	*char_pointer_value = 'Z';
	*int_pointer_value = 321;
	*double_pointer_value = 654.321;

	//변경된 일반 변수 데이터 출력
	cout << "char_value:" << char_value << endl;
	cout << "int_value:" << int_value << endl;
	cout << "double_value:" << double_value << endl;

	return 0;
	}

//다중 포인터
int sub(){
	int int_value = 123;

	int* int_pt_value = &int_value;
	int** int_pt_pt_value = &int_pt_value;
	int*** int_pt_pt_pt_value = &int_pt_pt_value;

	return 0;
}



