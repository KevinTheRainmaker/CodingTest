#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include<string.h>

char* solution(int n) {
	int i = 1;
	char* answer = (char*)malloc(sizeof(char)*3 * n); 
	memset(answer, NULL, sizeof(answer));

	while (i <= n) {
		if (i % 2 != 0) {
			strcat(answer, "수");
		}
		else {
			strcat(answer, "박");
		}
		i++;
	}
	return answer;
	free(answer);
}
int main() {
	int n;
	printf("Enter num: ");
	scanf("%d", &n);
	printf("Answer: %s",solution(n));
}