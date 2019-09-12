// 약수 알고리즘, 1부터 N까지 나누면서 나누어 지는 것을 저장하면 됌
// 10 = 1, 2, 5, 10
#include <stdio.h>

int main() {
	int n;

	scanf_s("%d", &n);

	for (int i = 1; i <= n; i++) {
		// 입력받은 숫자가 나누어 떨어지면 입력받은 숫자의 약수
		if(n % i == 0)
			printf("%d ",i);
	}

	return 0;
}