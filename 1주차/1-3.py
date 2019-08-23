# 방법을 변경해 보도록 합시다
# 입력받는 곳을 스택이라 생각합시다.
# 입력받은 값이 최대 범위이고 이전 범위를 포함한다면 스택에서 버립시다 
# 모든 입력을 받고나면 남은 범위에서 겹치지 않으면 OK
# 겹친다면 탈락!
def Day2Int(str_date):
    day_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    month, day = map(int,str_date.split('/'))
    total_day = 0
    for i in range(month-1):
        total_day += day_list[i]
    total_day += day
    print(total_day)
    return total_day

test_case = int(input())
day_stack_list = list() #빈 배열 선언
# test_case 만큼 반복
for i in range(test_case):
    # 여기에서 시작일, 끝나는 일 입력
    start_date, end_date = input().split()
    start_temp = None ; end_temp = None 
    if len(day_stack_list)==0:
        day_stack_list.append((Day2Int(start_date),Day2Int(end_date)))
    else:
        start_temp = Day2Int(start_date)
        end_temp = Day2Int(end_date)
# 현재 잘못되고 있는 조건 19.08.22
# 3 입력 -> 9/7 12/27, 1/25 12/17 (여기가 추가가 안됌), 2/27 3/5 (이상하게 이게 추가됌!)
        for k in range(len(day_stack_list)):
            if day_stack_list[k][0] > start_temp and day_stack_list[k][1] < end_temp and (start_temp,end_temp) not in day_stack_list:
                # 시작하는 일정과 끝나는 일정이 이전의 일정을 포함하는 경우
                day_stack_list.remove(day_stack_list[k])
                day_stack_list.append((start_temp,end_temp))                
            elif day_stack_list[k][0] == start_temp and day_stack_list[k][1] < end_temp and (start_temp,end_temp) not in day_stack_list:
                # 끝나는 일정만 더 긴 경우 ( 기준이 변경되야 함 )
                day_stack_list.remove(day_stack_list[k])
                day_stack_list.append((start_temp,end_temp))
            elif day_stack_list[k][0] > start_temp and day_stack_list[k][1] == end_temp and (start_temp,end_temp) not in day_stack_list:
                # 시작하는 일정만 더 빠른 경우 ( 기준이 변경되야 함 )
                day_stack_list.remove(day_stack_list[k])
                day_stack_list.append((start_temp,end_temp))
            else:
                if (start_temp,end_temp) not in day_stack_list:
                    day_stack_list.append((start_temp,end_temp))
                # 일정이 등록되어 있는 것들보다 이전인 경우 
            print(day_stack_list)
        
print(day_stack_list)
day_list = list()
# 최초 생각 , 끝날과 시작날의 차이를 구해서, 그것을 기준으로 sort를 하고 최고 범위의 index부터 고정해두고 범위에서 벗어나는지 안벗어나는지 확인
# 최고 범위를 정하고 나면, 안에서 꼬이는것을 체크하지 못함 
# 따라서 새로운 방법을 고안해야함
for i in range(len(day_stack_list)):#
    day_list.append(day_stack_list[i][1]-day_stack_list[i][0])
print(day_list)
# 정렬을 날이 긴 기준으로 정렬하자!!


# 5
# 5/1 7/1
# 5/1 7/1
# 4/3 8/4
# 3/4 9/3
# 3/4 10/3


# 10
# 6/14 10/20
# 6/17 8/25
# 4/3 7/22
# 5/4 9/3
# 9/7 12/27
# 1/25 12/17
# 2/27 3/5
# 5/11 10/20
# 2/12 7/14
# 2/27 8/13



# # return 시킬 숫자 flag -1:작음, 0: 같음, 1:보다큼
# # return 된 두개의 결과가 0이 되면, 범위에 상관 없는 것
# # 365일로 숫자로 표기해서 해당 범위 내에 있는지 없는지 확인
# def DayStr2Int(str_date):
#     day_list=[31,28,31,30,31,30,31,31,30,31,30,31]
#     month, day = map(int,str_date.split('/'))
#     total_day = 0
#     for i in range(month-1):
#         total_day += day_list[i]
#     total_day += day
#     return total_day
    
# testcase = int(input())
# # 각 경우마다 문자열로 시작일 마감일이 들어옴
# start_date = int(0); end_date = int(0)
# start_temp = 0 ; end_temp = 365
# flag = True
# for i in range(testcase):
#     start_input, end_input = input().split()
#     start_temp = DayStr2Int(start_temp,start_input)
#     end_temp = DayStr2Int(end_temp,end_input)
#     print(start_temp,end_temp)
#     if start_date < start_temp:
#         if end_date <= end_temp:
#             start_date = start_temp
#             end_date = end_temp
#         else:
#             print("No")
#             flag = False
#             break
#     elif end_date < start_temp:
#         pass 
#     elif end_temp < start_date:
#         pass
#     else:
#         if end_date <= end_temp:
#             pass
#         else:
#             print("No")
#             flag = False
#             break
# if flag:
#     print("Yes")

# # 시작일과 마감일안에 포함되거나
# # 시작일 마감일이 진행되었을때 밖의 범위에 존재하게 되면 됌!
# # 시작일과 마감일을 포함하여도 됌
# # 배열로해서 다 받게되면 10^5개의 테스트 케이스를 견디지 못할 것으로 판단함
# # 각 경우마다 괜찮은지 확인