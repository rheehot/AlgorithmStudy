# 에라토스테네스의 체
# 0번째 방부터 시작하기 때문에 0번째 방을 1로 생각
# 1부터 n까지 체크
# 1은 소수가 아니니 False로
# 2부터 루트(n)를 포함한 범위까지 체크를 하면 판별을 모두 다 할 수 있는 원리
# 2부터 루트(n)를 포함한 범위에서 True요소들의 배수를 다 제거한다.
# 배수를 표현하기 위해 i씩 증가를 시키고, i의 공배수중 i를 포함하지 않아야하니 i + i 부터 시작하게 한다.
# ex) 2의 베수 제거 -> 4부터 2씩 증가하면서 나머지 배수를 다 제거 (나머지까지니 입력받은 N 까지 입력)
# 이후 한번 더 반복을 통해 True 인 요소에 대한 count 를 진행
def solution(n):
    check_list = [True]*(n)
    count = 0
    check_list[0] = False
    max = int(n ** 0.5)
    for i in range(2,max+1):
        if check_list[i] == True:
            for j in range(i+i, n, i):
                check_list[j] = False
    print(check_list)
    for i in range(n):
        if check_list[i] == True:
            count += 1
    return count

print(solution(5))
print(solution(10))