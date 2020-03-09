# 딕셔너리로 하는 형태는 별로인것으로 판단
# 각 약수를 스택에 쌓는 방식으로 추가해서 카운팅하는것으로 해야겠음
# 첫 수와 끝 수의 범위를 파악

# 아래 결과로 알게된것
## 약수는 많은 테스트를 통해 2가 제일 많이 나온다는 것을 알게됌
## 두 수가 같을때만 문제
## 두 수가 같을 때 소수인지 아닌지 판단해서 소수가 아니라면 sqrt(N) 안에 약수가 나옴
## 소수라면 끝 수가 print되면 됌
first_number, second_number = map(int,input().split())
if first_number != second_number:
    print(2)
else:
    # 2로 나누어 떨어질 경우(유일한 짝수인 소수)
    if second_number % 2 == 0:
        print(2)
    else: # 나머지 소수는 홀수
        for i in range(3,second_number+1,2):
            if i**2 <= second_number: # 약수가 존재할 경우
                if second_number % i == 0:
                    print(i)
                    break
            else: #약수가 존재하지 않는 경우
                print(second_number)
                break


# if first_number > second_number:
#     seconde_number, first_number = first_number, second_number
# # 딕셔너리 생성
# dict_array = dict()
# # 해당 범위만큼 반복
# for i in range(first_number,second_number+1):
#     # 1 100 같은 1보다 작은 값이 존재할 수 있으니 해당 범위는 점프
#     if i < 2:
#         continue
#     else: # 실제 동작 부분
#         for d in range(2,i+1):
#             if i % d == 0: # 나누어 떨어질 때
#                 if (d in dict_array) == False: #값이 존재하지 않을 때, 딕셔너리 생성 후 값 추가
#                     dict_array[d] = 0
#                     dict_array[d] += 1
#                 else: # 값이 존재할 때 존재하는 값에 추가
#                     dict_array[d] += 1
# # 11 13에서와 같이 약수가 많이 존재하는 값이 중간에 끼여있을 경우 2가 작은 값이기 때문에 작은 값을 찾아야한다.
# dict_list = list(sorted(dict_array.items()))
# print(dict_list[0][0])
# max_value = 0
# min_key = 10**9
# for i in range(len(dict_list)):
#     if dict_list[i][1] >= max_value:
#         if dict_list[i][0] < min_key:
#             min_key = dict_list[i][0]
#             max_value = dict_list[i][1]
# print(min_key)
# # 키 리스트, 값 리스트 생성
# key_array = list(dict_array.keys())
# value_array = list(dict_array.values())
# # max 값 찾기 이후 해당 index 저장
# index_number = value_array.index(max(value_array))
# # 출력
# print(key_array[index_number])