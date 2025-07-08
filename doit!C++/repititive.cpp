//while문
#include <iostream>
using namespace std;

int main() {
	int count = 0;
	while (count < 5) {
		cout << "count:" << count << endl;
		count++;
	}
	return 0;
}

//do-while

int main() {
	int count = 0;
	do {
		cout << count << endl;
		count++;
	} while (count < 5);
	return 0;
}
//차이점
int main() {
	int i = 0;
	while (i < 0) {//조건식이 거짓이므로 반복문 실행 0번
		cout << "i is less than 0" << endl;
		i++;
	}

	int j = 0;
	do {
		cout << "j is less than 0" << endl;
		j++;
	} while (j < 0); //조건식이 거짓이나 반복문 1회 실행

	return 0;
}

//for문
int main() {
	for (int count = 0; count < 5; count++) { //(초기화;조건식;증감식)
		cout << "count:" << count << endl;
	}
	return 0;
}

//break
int main() {
	for (int count = 0; count < 10; count++) {
		cout << "count:" << count << endl;
		if (count == 5) {
			cout << "break로 반복문 탈출" << endl;
			break;
		}
	}
	cout << "반복문 종료" << endl;
	return 0;
}