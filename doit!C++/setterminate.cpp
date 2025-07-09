//종료처리 함수 set_terminate(종료처리함수);
#include <iostream>
#include <cstdlib>
using namespace	std;

void myterminate() {
	cout << "myterminate called" << endl;
	exit(-1); //프로그램 비정상적으로 종료
}

int main(void) {
	set_terminate(myterminate);
	throw 1; //예외발생
	return 0;//실행X
}

//catch가 없어 오류발생->set_termainate실행으로 종료됨