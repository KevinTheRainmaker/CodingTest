#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
	int answer = 0;
	int i, j;
	for (i = 1; i <= n; i++) {
		if (n%i == 0) {
			answer += i;
		}
	}
	return answer;
}
int main() {
	int n;
	printf("Enter integer: ");
	scanf("%d", &n);
	printf("The sum of aliquots is %d\n", solution(n));
	return 0;
}