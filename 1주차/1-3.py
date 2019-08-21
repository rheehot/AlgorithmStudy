# return 시킬 숫자 flag -1:작음, 0: 같음, 1:보다큼
# return 된 두개의 결과가 0이 되면, 범위에 상관 없는 것
# 365일로 숫자로 표기해서 해당 범위 내에 있는지 없는지 확인
def DayStr2Int(day_temp,str_date):
    day_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    month, day = map(int,str_date.split('/'))
    total_day = 0
    for i in range(month-1):
        total_day += day_list[i]
    total_day += day
    if day_temp > total_day:
        return total_day
    elif day_temp == total_day:
        return total_day
    else:
        return total_day
    ## 절대 안되는 경우 시작시간은 범위 안인데 , 끝시간이 범위 밖인경우
# 테스트 케이스 입력
testcase = int(input())
# 각 경우마다 문자열로 시작일 마감일이 들어옴
start_date = int(0); end_date = int(0)
start_temp = 0 ; end_temp = 365
flag = True
for i in range(testcase):
    start_input, end_input = input().split()
    start_temp = DayStr2Int(start_temp,start_input)
    end_temp = DayStr2Int(end_temp,end_input)
    print(start_temp,end_temp)
    if start_date < start_temp:
        if end_date <= end_temp:
            start_date = start_temp
            end_date = end_temp
        else:
            print("no")
            flag = False
            break
    else:
        if end_date <= end_temp:
            pass
        else:
            print("no")
            flag = False
            break
if flag:
    print("Yes")

# 시작일과 마감일안에 포함되거나
# 시작일 마감일이 진행되었을때 밖의 범위에 존재하게 되면 됌!
# 시작일과 마감일을 포함하여도 됌
# 배열로해서 다 받게되면 10^5개의 테스트 케이스를 견디지 못할 것으로 판단함
# 각 경우마다 괜찮은지 확인