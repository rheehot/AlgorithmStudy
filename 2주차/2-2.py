'''
입력
3
A
BC
DEFG
출력
7
11
'''

# 2^20 = 백만개
test_case = int(input()) # 입력할 갯수?
temp = list()# 난중에 최종 값을 더하는 곳
temp_list = list() # 빈 리스트 생성 A, B,C 와 같은 문자들을 입력받기 위함
for i in range(test_case):
    input_str = input()
    for j in range(len(input_str)):
        temp_list.append(ord(input_str[j])-64)
        temp_list.append(ord(input_str[j])-64)
    if i == 0:
        temp = temp_list[::]
        temp_list = list()
        print(temp)
    else:
        temp = temp + temp # 여기서 임의로 더해버리면 안되고, 
        for i in range(len(temp)):
            temp[i] = temp[i] + temp_list[i]
        temp_list = list()
        print(temp)
print(min(temp))
print(max(temp))
    # 이렇게 하면 다음번에 입력되는 값에 더해질 수 있다.
# a:1 b:2 이런식으로 추가하려했는데 생각다시