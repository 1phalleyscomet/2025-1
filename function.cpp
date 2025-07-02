/*반환형식 함수명(매개변수){함수몸체}
반환형식: 함수가 반환할 값읠 자료형, 없을경우 void
함수명: 숫자,공백X
매개변수: 함수가 호출될 때 전달받은 값을 저장하는 변수(지역), 비우거나 void 표시 가능
함수 몸체: 기능 정의
*/

#include <iostream>
using namespace std;

int add(int_x, int_y) {
	int result = _x + _y;
	return result;
}

int main() {
	int add_result = and (2, 3);
	cout << "add 함수 결과:" << add_result << endl;

	return 0;
}
//일반 변수 매개변수로 활용
void change_nagative(int _val) {
	if (_val > 0) {
		_val = -_val;
		//반환값 return 없음
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

	//main의 변수에 영향X

}

//포인터 변수를 매개변수로 사용
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

	//main의 변수에 영향O

}

//배열을 매개변수로 사용

int average(int_array[], int _count) {
	int sum = 0;
	for (int i = 0; i < _count; i++) {
		sum += _array[i];
	}
	return (sum / _count);
}

int main() {
	int score[5] = { 90,75,80,100,65 };
	cout << "평균점수:" << average(score, 5) << endl;

	return 0;

	//매개변수 _array배열 데이터 변경 시 main에 score 배열 데이터 변경
}

/*구조체
struct 구조체{
std::string name;
int age;
float height;
float weight; };

하나 이상의 변수를 묶어 새로운 자료형으로 정의
배열선언 가능
*/

//구조체를 매개변수로 사용하기

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
	check_age(adult, 3); //구조체 배열 시작 주소 전달

	return 0;
}
