# 동전 줍기 대회
# 각 참가자 앞에 동전은 일렬로 놓여있으며, 각 동전은 줍거나 줍지 않을 수 있습니다.
# 이때, 서로 떨어져있는 동전은 주울 수 없으며 주운 동전들은 모두 일렬 순서대로 연속되어야 합니다.
# 동전 중에는 음의 가치를 가지는 동전도 있습니다.
# 대회가 끝나면 각 참가자들은 자신이 주운 동전들의 가치의 합에 해당하는 상금을 받습니다(주운 동전들의 가치의 합이 음수라면 오히려 돈을 내야 합니다).

# #1
# 입력
# 6
# 10 -5 3 2 4 -7
# 출력
# 14

# #2
# 입력
# 10
# -6 -9 -7 8 3 -5 -2 -3 -7 0
# 출력
# 11

# #3
# 입력
# 100
# 94 74 99 50 85 17 93 13 79 4 18 58 52 56 84 90 54 2 35 79 97 50 6 47 47 20 95 91 78 35 56 93 2 55 30 84 51 3 58 97 82 4 70 90 65 46 57 28 99 13 24 15 66 93 1 99 63 82 67 28 75 20 15 24 26 33 5 38 11 36 96 45 63 50 11 20 85 0 50 19 69 78 79 95 33 53 78 43 33 39 92 21 59 67 81 81 80 48 32 36
# 출력
# 5242

input_case = int(input())
test_list = list(map(int,input().split()))
plus_temp = 0
minus_temp = 0
plus_result = []
minus_result = []
plus_flag = False
# 무조건 양수부터 주워야 한다고 생각된다.
# 그래서 처음부터 양수인 부분까지를 새로 도출해 낸다
# 시작해 내고 나서, 각 요소들을 양수인 구간부터 더하면 되지 않을까?
for i in range(input_case):
    if test_list[i] > 0:
        plus_flag = True
    if plus_flag == True:
        if test_list[i] > 0:
            if minus_temp != 0:
                minus_result.append(minus_temp)
                minus_temp = 0
            plus_temp += test_list[i]
        elif test_list[i] == 0:
            pass
        else:
            if plus_temp != 0:
                plus_result.append(plus_temp)
                plus_temp = 0
            minus_temp += test_list[i]
if plus_temp != 0:
    plus_result.append(plus_temp)
    plus_temp = 0
print(plus_result,minus_result)
# 여기서 조합을 써보자