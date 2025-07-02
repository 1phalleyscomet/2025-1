//�迭 ����
/*�ڷ��� �迭�̸�[ũ��]={��1,��2,...,��n};*/
//���� �迭
#include <iostream>
using namespace std;

int main() {
	int lotto[45] = { 1,2,3,...,45 };

	cout << "Today's Lotto:" << lotto[1] << "," << lotto[7] << "," << lotto[14] << "," << lotto[27] << endl;

	//�迭 ������ �޸� �ּ� Ȯ���ϱ�
	cout << "lotto[0] address:" << &lotto[0] << endl;
	cout << "lotto[1] address:" << &lotto[1] << endl;
	cout << "lotto[2] address:" << &lotto[2] << endl;

	//�迭 ������ �ּҿ� ������ ������ ��� ��
	cout << "(lotto+0) address:" << lotto + 0 << endl; //������ �������� �迭 ���ҿ� ����
	cout << "(lotto+1) address:" << lotto + 1 << endl;
	cout << "(lotto+2) address:" << lotto + 2 << endl;

	/*
	&lloto[0] == lotto + 0
	&�迭����[�ε���] == �迭����+�ε���

	lotto->ù��° ���� �ּ� &lotto[0] ����Ŵ
	*/

	//�迭�� ������ ����
	int array[5] = { 1,2,3,4,5 };
	int* pointer_array = array;

	cout << "array: " << array << endl;
	cout << "pointer_array: " << pointer_array << endl << endl;

	cout << "sizeof(array): " << sizeof(array) << endl;
	cout << "sizeof(pointer_array) : " << sizeof(pointer_array) << endl;
	//�迭 ��ü ũ�� 20byte
	//������ ���� ũ�� 8byte

	//������ �������� ����
	cout << "Today's Lotto:" << *lotto << "," << *(lotto + 7) << "," << *(lotto + 14) << "," << *(lotto + 27) << endl;


	return 0;
}