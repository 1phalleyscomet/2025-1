//const ���� ���ȭ
//�ʱ�ȭ �ʼ�

#include <iostream>
using namespace std;

int main() {
	const int a = 1;
	a = 2;  //������ ���� �߻�

	return 0;
}

//������ ���� ���ȭ

int main() {
	int a = 0;
	const int* ptr = &a; //*ptr ���ȭ
	a = 1; //������ ���
	*ptr = 2; //������ ����

	return 0;
}

int main() {
	int a = 0;
	int b = 1;
	int* const ptr = &a; //ptr�� ���ȭ
	a = 1;
	ptr = &b; //������ ����

	return 0;
}

//*ptr ���ȭ=������ ������ ����Ű�� ���� ���ȭ
//ptr���ȭ=������ ���� ��ü�� ���ȭ
//const ��� �� �ش� �� ���� X