//조건에 따른 분기 if/switch
/*if(조건식){실행문}*/
#include <iostream>
using namespace std;
int main() {
	int input_number;

	cout << "정수입력:";
	cin >> input_number;

	if (input_number > 0) {
		cout << "입력한 수는 양수입니다." << endl;
	}
	else if (input_number < 0) {
		cout << "입력한 수는 음수입니다." << endl;
	}
	else {
		cout << "입력한 수는 0입니다." << endl;
	}
	return 0;
}

//중괄호 생략
//실행 구문이 하나일 때

int main() {
	int input_number;

	cout << "정수입력:";
	cin >> input_number;

	if (input_number > 0)
		cout << "입력한 수는 양수 입니다." << endl;
	else if (input_number < 0)
		cout << "입력한 수는 음수입니다." << endl;
	else
		cout << "입력한 수는 0입니다." << endl;
	return 0;
}
//switch
int main() {
	int input_number;

	cout << "1~5 정수 입력:";
	cin >> input_number;

	switch (input_number) {
	case 1:
		cout << "입력한 수는 1입니다." << endl;
		break;
	case 2:
		cout << "입력한 수는 2입니다." << endl;
		break;
	case 3:
		cout << "입력한 수는 3입니다." << endl;
		break;
	case 4:
		cout << "입력한 수는 4입니다." << endl;
		break;
	case 5:
		cout << "입력한 수는 5입니다." << endl;
		break;
	default:
		cout << "입력한 수는 범위 밖입니다." << endl;
		break;
	}
	return 0;
}
//break 없을 시 참인 case부터 모든 구문 실행