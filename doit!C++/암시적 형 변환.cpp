#include <iostream>
using namespace std;

int main() {
	float float_value = 1.5f;

	double double_value = float_value; //�°�:������ ����x
	int int_value = float_value; //������ ����o

	cout << "float_value:" << float_value << endl;
	cout << "double_value:" << double_value << endl;
	cout << "int_value:" << int_value << endl;

	return 0;
}

/*
implicit cast(�Ͻ��� ����ȯ) �����Ϸ��� �ڵ����� ����
explicit cast(����� ����ȯ) �����ڰ� �ǵ������� ���� ����
*/

//����ȯ ��
int sub() {
	int int_a = 10;
	int int_b = 5;

	int int_avg = (int_a + int_b) / 2;
	float float_avg1 = (int_a + int_b) / 2; //������ ����
	float float_avg2 = float(int_a + int_b) / 2; //����� ����ȯ

	cout << "int_avg:" << int_avg << endl;
	cout << "float_avg1:" << float_avg1 << endl;
	cout << "float_avg2:" << float_avg2 << endl;

	return 0;
}