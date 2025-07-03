//������ �� �ٸ� ��Ī�� �ο���
//�Ű������� �Ϲ� ������ ����
#include <iostream>
using namespace std;

void swap(int a, int b) {
	//swap�Լ� �� ��ȯ �� a,b��

	cout << "[swap func] before swap, a: " << a << "b:" << b << endl;

	int temp = a;
	a = b;
	b = temp;

	//swap�Լ� �� ��ȯ �� a,b��
	cout << "[swap func] after swap, a: " << a << "b:" << b << endl;

}

int main() {
	int a = 5;
	int b = 10;

	//swap�Լ� ȣ�� �� a,b��
	cout << "[main] before swap, a: " << a << "b:" << b << endl;
	swap(a, b);

	//swap�Լ� ȣ�� �� a,b��
	cout << "[main] after swap, a: " << a << "b:" << b << endl;

	return 0;
}

//swap �Ű������� ���� �� ���� ��ȯ �Լ�
//���� ���� ȣ��(call by value) ���� �����ϴ� ȣ�� ���, ���� �Ű������� ����->���ο� ����(main�Լ� ������ ��ȭX)

/*���۷��� ���� ����
* �ڷ��� &���۷��� ���� �̸�=��� ���� �̸�; */

//���۷��� ���� ����
void swap(int& ref_a, int& ref_b) {
	cout << "[swap func] before swap, ref_a: " << ref_a << "ref_b:" << ref_b << endl;

	int temp = ref_a;
	ref_a = ref_b;
	ref_b = temp;
	cout << "[swap func] after swap, ref_a: " << ref_a << "ref_b:" << ref_b << endl;


}

int main() {
	int a = 5;
	int b = 10;

	cout << "[main] before swap, a: " << a << "ref_b:" << b << endl;

	swap(a, b);

	//swap�Լ� ȣ�� �� a,b��
	cout << "[main] after swap, a: " << a << "b:" << b << endl;

	return 0;
}

//���� ���� a,b->ref_a,ref_b ��Ī ȹ��
//������ ���� ȣ��(call by reference) ��ȣ����(main)���� �״�� �̿�
//�ݵ�� ���� ���� ����
//���� ���� ��� ���� �Ұ�
//��� ���� �Ұ�