// ��Ŭ���� ȣ������ �̿��� �ִ����� ���ϱ�
// �Է°��� �� ��
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
			printf("�� ���� �ִ�����(GCD, Greatest Common Divisor)�� %d �Դϴ�.", GCD);
			printf("�� ���� �ּҰ����(LCM, Lower Common Multiplier)�� %d �Դϴ�.", LCM);
			break;
		}
		a = b;
		b = r;
	}
}
*/