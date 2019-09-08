# # 첫째 줄에 연구실의 크기를 나타내는 정수 R, C가 주어집니다. (단, 1< 1000)

# # 둘째 줄부터 R줄에 걸쳐서 길이 C인 문자열이 주어집니다. 문자열에 포함된 문자가 의미하는 바는 다음과 같습니다. 불은 하나 이상 있음이 보장됩니다.

# # '.' : 빈 칸(불이 번질 수 있음)
# # '#' : 벽(불이 번질 수 없음)
# # '&' : 원준이
# # '@' : 불

# # 내가 생각하는 가장 쉬운 방법은 불을 퍼트려 보는 방법이다.
# # 반복 횟수는 칸수만큼만
# row, column =map(int,input().split())
# print(row,column)
# test_list = list()
# for i in range(column):
#     test_list.append(list(input()))

# count = 0
# while row*column > count:
#     for i in range(column):
#         for j in range(row):
#             if test_list[i][j] == '_':
#                 pass
#             elif test_list[i][j] == '#':
#                 pass
#             elif test_list[i][j] == '&':
#                 pass
#             else:
#                 #퍼져나가야지 , 이렇게 모든 경우를 적어주는게 맞는건가?....

#                 if i == 0 and j == 0:
#                     if test_list[i][j+1] == '_':
#                         test_list[i][j+1] = '@'
#                     if test_list[i+1][j] == '_':
#                         test_list[i+1][j] = '@'
#                 elif i == 0 and test_list[i][j+1] != '#':
#                     if test_list[i][j+1] == '_':
#                         test_list[i][j+1] = '@'
#                     if test_list[i+1][j] == '_':
#                         test_list[i+1][j] = '@'
#                 elif i != 0 and 
#     count += 1

##############################################################
# 형 미안해여.. 답지 보고 이해해볼께요. 3시간 봐도 모르겠습니다.  #
##############################################################