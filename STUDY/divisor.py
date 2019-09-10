# 약수 구하는 소스 코드 Divisor , 특정 정수를 나누어 떨어지게 하는 수
# ex) 10의 약수 1,2,5,10
# 보통 약수를 구하는 방법 1부터 끝까지 나누면서 진행해봄
def divisor(temp,num):
    for i in range(1,num+1): # 1부터 나누고 끝 자리가 1자리 적게 계산이 되니까 그거에 따른 추가 값을 입력을 해주어야 한다
        if num % i == 0:
            temp.append(i)

if __name__=="__main__":
    temp = list()
    divisor(temp,int(input()))
    print(temp)