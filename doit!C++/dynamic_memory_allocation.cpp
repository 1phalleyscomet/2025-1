/*����ũ�� �迭���� ��)
char char_array[10];
int int_array[500];
float float_array[1000];*/

//���� �޸� �Ҵ�
//�ڷ��� *������ = new �ڷ���;

//���� �޸� ����
//delete ������;

#include <iostream>
using namespace std;

int main() {
	int* pt_int_value = new int;

	*pt_int_value = 100;
	cout << *pt_int_value << endl;

	delete pt_int_value;

	//�迭 ������ ���� �޸� �Ҵ�� ����
	// �ڷ��� *������ = new �ڷ���[ũ��];
	// delete[] ������;

	int* pt_int_array_value = new int[5];
	
	for (int i = 0; i < 5; i++) {
		pt_int_array_value[i] = i; //�Ҵ�� �迭 ������ 0-4 ������� �ֱ�
	}

	for (int i = 0; i < 5; i++) {
		cout << pt_int_array_value[i] << endl; //�迭 ���� ���
	}

	delete[] pt_int_array_value;

	/*���� �޸� �Ҵ��� �����ϴ� ����
	�Ϲݺ���->stack�� �Ҵ�
	->�Լ� ��ȯ �� �ڵ� �Ҹ�
	
	�����Ҵ纯��->heap�� �Ҵ�
	->����� ���� �� �Ҵ� ���� ����->�޸� ����, �޸� ���� ���*/

	return 0;
}