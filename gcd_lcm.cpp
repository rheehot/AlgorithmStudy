// 유클리드 호제법을 이용한 최대공약수 구하기
// 입력값은 두 개
/*
#include<stdio.h>

int main(void) {
	int a, b, r;
	int org_a, org_b;
	int GCD,LCM;
	scanf_s("%d %d", &a, &b);
	org_a = a, org_b = b;
	while (true) {
		r = a % b;
		if (a % b == 0) {
			GCD = b;
			org_a /= GCD;
			org_b /= GCD;
			LCM = org_a * org_b * GCD;
			printf("두 수의 최대공약수(GCD, Greatest Common Divisor)는 %d 입니다.", GCD);
			printf("두 수의 최소공배수(LCM, Lower Common Multiplier)는 %d 입니다.", LCM);
			break;
		}
		a = b;
		b = r;
	}
}
*/