
//assertion 예상치 못한 상황에서 프로그램 동작 중단
#include <iostream>
#include <cassert>

using namespace std;

void print_number(int* _pt_int) {
	assert(_pt_int != NULL); //디버그 모드에서 NULL인지 검사
	cout << *_pt_int << endl;
}

int main() {
	int a = 100;
	int* b = NULL;
	int* c = NULL;
	b = &a;
	print_number(b);
	print_number(c);

	return 0;
}