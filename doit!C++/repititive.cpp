//while��
#include <iostream>
using namespace std;

int main() {
	int count = 0;
	while (count < 5) {
		cout << "count:" << count << endl;
		count++;
	}
	return 0;
}

//do-while

int main() {
	int count = 0;
	do {
		cout << count << endl;
		count++;
	} while (count < 5);
	return 0;
}
//������
int main() {
	int i = 0;
	while (i < 0) {//���ǽ��� �����̹Ƿ� �ݺ��� ���� 0��
		cout << "i is less than 0" << endl;
		i++;
	}

	int j = 0;
	do {
		cout << "j is less than 0" << endl;
		j++;
	} while (j < 0); //���ǽ��� �����̳� �ݺ��� 1ȸ ����

	return 0;
}

//for��
int main() {
	for (int count = 0; count < 5; count++) { //(�ʱ�ȭ;���ǽ�;������)
		cout << "count:" << count << endl;
	}
	return 0;
}

//break
int main() {
	for (int count = 0; count < 10; count++) {
		cout << "count:" << count << endl;
		if (count == 5) {
			cout << "break�� �ݺ��� Ż��" << endl;
			break;
		}
	}
	cout << "�ݺ��� ����" << endl;
	return 0;
}