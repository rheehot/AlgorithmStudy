# 2^20 = 백만개
test_case = int(input()) # 입력할 갯수?
temp = list()# 난중에 최종 값을 더하는 곳
temp_list = list() # 빈 리스트 생성 A, B,C 와 같은 문자들을 입력받기 위함
new_temp = list() # ABAB 의 형태가 아닌 AABB로 옮기기 위함
for i in range(test_case):
    input_str = input()
    for j in range(len(input_str)): # 다음 과정에서 어짜피 2배로 값을 더해주어야 하기 때문에 추가해 주는 작업
        temp_list.append(ord(input_str[j])-64)
        temp_list.append(ord(input_str[j])-64)
    if i == 0: # 초기화 과정, 값을 temp로 옮기고 더해주기 위함
        temp = temp_list[::]
        temp_list = list()
    else:   
        for k in range(len(temp)): # 초기에 저장된 값을 AABB의 형태로 저장히기 위해서 더해주는 과정
            new_temp.append(temp[k])
            new_temp.append(temp[k])
        temp = list()
        temp = new_temp[::]
        new_temp = list()
        for k in range(len(temp)): # 실질적으로 합해져서 최종 결과로 나오는 과정
            temp[k] = temp[k] + temp_list[k]
        temp_list = list()
print(min(temp))
print(max(temp))
    # 이렇게 하면 다음번에 입력되는 값에 더해질 수 있다.
# a:1 b:2 이런식으로 추가하려했는데 생각다시