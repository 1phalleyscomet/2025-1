#include <iostream>
#include <string>
using namespace std;

int main() {
	int customer_num = 0;

	cout << "�湮 �մ�:";
	cin >> customer_num; //�մ� �� �Է�

	string* bread = new string[customer_num]; //�մ� �� ��ŭ string �迭 ����

	for (int i = 0; i < customer_num; i++) {
		bread[i] = "��_" + to_string(i); //��_���� ���·� �迭�� ���� //to_string() ���ڸ� ���ڿ��� ��ȯ�ϴ� �Լ�

	}

	cout << endl << "--����� ��--" << endl;
	for (int i = 0; i < customer_num; i++) {
		cout << *(bread + i) << endl;
	}

	delete[] bread;

	return 0;

}

/* ������ ������ �� �����Ͱ� ��ȿ�� �޸𸮸� ����Ű���� Ȯ��->segmentation fault, runtime error �߻�
�Ҵ�� �޸� ������ ����� ������ ���� X
�Ҵ� ������ �޸� ������ X */