//static �ڵ�����->�������� ���� ��ȿ ���� ����
// ��������->�������� ��ȯ

#include <iostream>
using namespace std;

void func() {
	int a = 10;
	static int b = 10;

	a++;
	b++;

	cout << "a:" << a << ",b:" << b << endl;

}

int main() {

	func();
	func();
	func();
	func();
	func();

	return 0;
}

/*�������� a->func�Լ� ȣ�� �� ���� ����, ���� �� �Ҹ�
b-> �������� func�Լ� ȣ�� ��ŭ �� ���� *�ݵ�� �ʱ�ȭ* */

int getNewID() {
	static int ID = 0;
	return ++ID;
}

int main() {
	cout << "ID:" << getNewID() << endl;
	cout << "ID:" << getNewID() << endl;
	cout << "ID:" << getNewID() << endl;
	cout << "ID:" << getNewID() << endl;

	return 0;
}

/*�������� ->stack ���� ����
��������->data ���� ����(���α׷� ���� �� �Ҵ�, ���� �� ����)*/

