# 값 입력
num = input()
# 나올 수 있는 값 12, 21
one_two = 0
two_one = 0
# 1 혹은 2 로부터 시작되는 구간 찾아 정리
for i in range(len(num)):
    if num[i] == '1' or num[i] == '2':
        num = num[i:]
        break
# 1,2 가 나오는 경우를 찾아내고 해당 범위를 잘라낸 후 종료
for i in range(len(num)):
    if num[i]=='1' and num[i+1]=='2':
        one_two += 1
        num = num[:i] + num[i+2:]
        break
# 2,1 가 나오는 범위를 찾아내고 해당 범위를 잘라낸 후 종료
for i in range(len(num)):
    if num[i]=='2' and num[i+1]=='1':
        two_one += 1
        num = num[:i] + num[i+2:]
        break

## 12 21 이 한번씩 나온 경우 
if one_two == 1 and two_one == 1:
    print('Yes')
else: # 안나온경우
    print("No")