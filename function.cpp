/*��ȯ���� �Լ���(�Ű�����){�Լ���ü}
��ȯ����: �Լ��� ��ȯ�� ���� �ڷ���, ������� void
�Լ���: ����,����X
�Ű�����: �Լ��� ȣ��� �� ���޹��� ���� �����ϴ� ����(����), ���ų� void ǥ�� ����
�Լ� ��ü: ��� ����
*/

#include <iostream>
using namespace std;

int add(int_x, int_y) {
	int result = _x + _y;
	return result;
}

int main() {
	int add_result = and (2, 3);
	cout << "add �Լ� ���:" << add_result << endl;

	return 0;
}
//�Ϲ� ���� �Ű������� Ȱ��
void change_nagative(int _val) {
	if (_val > 0) {
		_val = -_val;
		//��ȯ�� return ����
	}
}

int main() {
	int a = 3, b = -3;

	cout << "a:" << a << endl;
	cout << "b:" << b << endl;

	change_negative(a);
	change_negative(b);

	cout << "change_nagative(a):" << a << endl;
	cout << "change_nagative(b):" << b << endl;

	return 0;

	//main�� ������ ����X

}

//������ ������ �Ű������� ���
void change_negative(int* _val) {
	if (*_val > 0) {
		*_val = -*(_val);
	}
}

int main() {
	int a = 3, b = -3;
	cout << "a:" << a << endl;
	cout << "b:" << b << endl;

	change_negative(&a);
	change_negative(&b);

	cout << "change_nagative(a):" << a << endl;
	cout << "change_nagative(b):" << b << endl;

	return 0;

	//main�� ������ ����O

}

//�迭�� �Ű������� ���

int average(int_array[], int _count) {
	int sum = 0;
	for (int i = 0; i < _count; i++) {
		sum += _array[i];
	}
	return (sum / _count);
}

int main() {
	int score[5] = { 90,75,80,100,65 };
	cout << "�������:" << average(score, 5) << endl;

	return 0;

	//�Ű����� _array�迭 ������ ���� �� main�� score �迭 ������ ����
}

/*����ü
struct ����ü{
std::string name;
int age;
float height;
float weight; };

�ϳ� �̻��� ������ ���� ���ο� �ڷ������� ����
�迭���� ����
*/

//����ü�� �Ű������� ����ϱ�

struct Person {
	std::string name;
	int age;
	float height;
	float weight;
};

void check_age(Person* _adult, int _count) {
	for (int i = 0; i < _count; i++) {
		if (_adult[i].age >= 25) {
			cout << "name:" << _adult[i].name << endl;
			cout << "age:" << _adult[i].age << endl;
			cout << "height:" << _adult[i].height << endl;
			cout << "weight:" << _adult[i].weight << endl;
		}
	}
}

int main() {
	Person adult[3] = {
		{"brain",24,180,70},
		{"jessica",22,165,55},
		{"james",30,170,65},
	};
	check_age(adult, 3); //����ü �迭 ���� �ּ� ����

	return 0;
}
