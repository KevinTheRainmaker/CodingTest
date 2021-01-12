#include <stdio.h>

/*int pow(int x, int y) {
	if (y == 0) {
		return 1;
	}
	return x * pow(x, y - 1);
}
int solution(int n) {
	int answer = 0;
	int ten = 10;
	int sum;
	for (int i = 10; i >= 0; i--) {
		ten = pow(10, i);
		sum = n / ten;
		n = n - (sum * ten);
		answer += sum;
	}
	return answer;
}*/
//이 위의 코드는 그닥 좋지 않다고 생각된다.

int solution(int n) {
	int answer = 0;
	while (n != 0) {
		answer += n % 10;
		n = n / 10;
	}
	return answer;
}

int main() {
	int n;
	printf("Enter the integer: ");
	scanf("%d", &n);
	printf("The sum of each digit of the integer you enter is %d\n", solution(n));
	return 0;
}