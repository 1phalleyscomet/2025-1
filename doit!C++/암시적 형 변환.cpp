#include <iostream>
using namespace std;

int main() {
	float float_value = 1.5f;

	double double_value = float_value; //승격:데이터 유실x
	int int_value = float_value; //데이터 유실o

	cout << "float_value:" << float_value << endl;
	cout << "double_value:" << double_value << endl;
	cout << "int_value:" << int_value << endl;

	return 0;
}

/*
implicit cast(암시적 형변환) 컴파일러가 자동으로 변경
explicit cast(명시적 형변환) 개발자가 의도적으로 직접 변경
*/

//형변환 비교
int sub() {
	int int_a = 10;
	int int_b = 5;

	int int_avg = (int_a + int_b) / 2;
	float float_avg1 = (int_a + int_b) / 2; //데이터 유실
	float float_avg2 = float(int_a + int_b) / 2; //명시적 형변환

	cout << "int_avg:" << int_avg << endl;
	cout << "float_avg1:" << float_avg1 << endl;
	cout << "float_avg2:" << float_avg2 << endl;

	return 0;
}