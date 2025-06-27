#include <iostream>
//#include <string> 표준 라이브러리의 std::string 사용을 위한 헤더 추가 *iostream에 포함, 생략가능
using namespace std;

int sub() {
	string string_value("hello");
	cout << string_value << endl;
	string_value = "world"; //따옴표 주의
	cout << string_value << endl;

	return 0;
}
/*문자 literal
''(작은따옴표) 단일문자
std::cout<<"hello world\n";
std::cout<<"helloworld"<<'\n';
*/

/*
사용자 정의 리터럴
반환타입 operator"" 리터럴접미사(매개변수)
*/

const long double km_per_mile = 1.609344L;

long double operator"" _km(long double val) {
	return val; //작업 없이 반환
}

long double operator"" _mi(long double val) {
	return val * km_per_mile;
}

int main() {
	long double distance_1 = 1.0_km;
	long double distance_2 = 1.0_mi;

	cout << distance_1 + distance_2 << " km" << endl;

	return 0;
}