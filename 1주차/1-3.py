# return 시킬 숫자 flag -1:작음, 0: 같음, 1:보다큼
# return 된 두개의 결과가 0이 되면, 범위에 상관 없는 것
def DayStr2Int(start_m, start_d, end_m, edm_d, start_date, end_date):
    s_month, s_day = start_date.split('/')
    e_month, e_day = end_date.split('/')
    if start_m > s_month: # 시작일이 범위 이전인 경우
        start_m = s_month
        start_d = s_day #시작일 보다 무조건 month 가 작기 때문에 저장만 하면 됌
        if end_m < e_month:
            end_d = e_day #달이 더 높기 때문에 항상 참
        elif end_m == e_month:
            if end_d < e_day: # 달은 같지만 입력받은 값이 더 늦는 경우(참)
                end_d = e_day
            elif end_d == e_day: # 이 또한 참, 시작일이 이전이기 때문에 (참)
                end_d = e_day # 굳이 필요없지만 일단 넣어두자
            else:
                pass# 이 경우는 거짓에 해당함,
        else:
            pass# 이 경우도 거짓에 해당함
    elif start_m == s_month: # 시작 달이 같은 경우
        start_m = s_month # 일단 저장할 필요 없지만 저장
        if start_d < s_day: # 이 경우 범위가 작아야 하므로 end_d가 작아야함
            pass
        elif start_d == s_day:
            pass # 같은 날 시작 , 이날 시작한 경우 끝나는 날의범위가 작아도 되고 커도됌
        else:
            pass # 시작일이 더 이전이므로 끝나는 날도 더 늦어야한다.
    else: # 시작달이 범위 안인 경우, 무조건 안에서 끝나거나 같아야한다.
        pass #end_d에 관한 내용만 작성을 진행하면 됌
        
# 테스트 케이스 입력
testcase = int(input())
# 각 경우마다 문자열로 시작일 마감일이 들어옴
start_month = int(0); start_day = int(0)
end_month = int(0); end_day = int(0)
for i in range(testcase):
    start_input, end_input = input().split()
    DayStr2Int(start_month,start_day,end_month,end_day,start_input,end_input)
print(start_month,start_day)
# 시작일과 마감일안에 포함되거나
# 시작일 마감일이 진행되었을때 밖의 범위에 존재하게 되면 됌!
# 시작일과 마감일을 포함하여도 됌
# 배열로해서 다 받게되면 10^5개의 테스트 케이스를 견디지 못할 것으로 판단함
# 각 경우마다 괜찮은지 확인