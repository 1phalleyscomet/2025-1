//����ó�� �Լ� set_terminate(����ó���Լ�);
#include <iostream>
#include <cstdlib>
using namespace	std;

void myterminate() {
	cout << "myterminate called" << endl;
	exit(-1); //���α׷� ������������ ����
}

int main(void) {
	set_terminate(myterminate);
	throw 1; //���ܹ߻�
	return 0;//����X
}

//catch�� ���� �����߻�->set_termainate�������� �����