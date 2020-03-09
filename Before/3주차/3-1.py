# 외계인과 용돈 기입장

# 입력
day, test_case = map(int,input().split())
string_money = list(map(str,input().split()))
money = list()
for i in range(day):
    if string_money[i][0] == '+':
        money.append(int(string_money[i][1:]))
    else:
        money.append(int(string_money[i]))
# 호출
for i in range(test_case):
    a, b = map(int,input().split())
    temp = sum(money[a-1:b])
    if temp> 0:
        print('+'+str(temp))
    else:
        print(str(temp))