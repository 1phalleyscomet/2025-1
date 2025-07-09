/*�Լ��� ���ܸ� ������ ������ ���
int func() noexcept*/
/*�Լ��� ���ܸ� �������� Ȯ��
bool does_not_throw=noexcept(my_function());*/

//noexcept�Լ����� ���� ������
#include <iostream>
using namespace std;

void real_noexcept() noexcept {
	cout << "real_noexcept" << endl;
}

void fake_noexcept() noexcept {
	cout << "fake_noexcept" << endl;
	throw 1;
}

int main() {
	real_noexcept();

	try {
		fake_noexcept();
	}
	catch (int exec) {
		cout << "catch" << exec << endl;
	}

	return 0;
}

//runtime error