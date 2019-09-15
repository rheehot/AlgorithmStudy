#include<stdio.h>

// 포인터란? 
// 값을 저장하는 것이 아닌, 값의 위치를 저장하는 변수

int main() {
	int *myPointer;
	int a;
	
	a = 5;
	myPointer = &a; //a의 주소값을 저장
	// 결론 a의 위치를 저장하기 위해서 *을 붙임
	printf("myPointer 값 : %d \n",*myPointer);//myPoiner 값에 저장된 값 출력
    // 만약 그냥 myPointer를 출력하게 된다면, 해당 값은 myPointer의 위치 값이 나옴
	printf("a : %d \n",a);//a의 값 출력
}