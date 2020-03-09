# BFS / DFS 공부하기 싫어서 안했는데 한번 따라해보면서 알아가보자.
# BFS(Breath First Search, 너비 우선 탐색)
# graph = {
#     'A': ['B'],
#     'B': ['A', 'C', 'H'],
#     'C': ['B', 'D', 'G'],
#     'D': ['C', 'E'],
#     'E': ['D', 'F'],
#     'F': ['E'],
#     'G': ['C'],
#     'H': ['B', 'I', 'J', 'M'],
#     'I': ['H'],
#     'J': ['H', 'K'],
#     'K': ['J', 'L'],
#     'L': ['K'],
#     'M': ['H']
# }
# 갈 수 있는 모든 흐름이 작성 되어 있는데.. 흠.. 인접 행렬, 인접 리스트인가 그것을 써야하는 건가?
# 위의 흐름대로 풀려면 갈 수 있는 곳과 갈 수 없는 곳을 표현가능한 형태로 표현해야한다.
# 그럼 '(0,0)' ['(0,1)' '(1,0)'] 이런식으로 표현해야하나?
# 갈 수 있는 곳은 리스트로 해서 튜플로 작성해 주고 갈 수 없는 곳은 빈 리스트로 놓은 다음 graph 라는 튜플에 저장을 해보자.
# 저장한 다음 해당 불이 발생한 지점을 읽어들어 갈 수 있는 지점의 최소 값을 고르면 되는 것 아닌가?
# 가만히 생각해보니까 불로 부터 시작하는 것이 아니라 연구원으로 부터 시작을 하는 것이 좋지아니한가?

# 리스트의 형태로 넣어주고 해당 값을 기준으로 갈 수 있는 곳과 갈 수 없는 곳을 설정 할 수 있도록 해야한다.
def root_graph(start_point,temp_list,target,map_list):
    print(map_list)
    for i in start_point:
        if map_list[i[0]][i[1]] == "_" and i[0] == 0 :
            if i[1] != "dsnLKFnzlkdfndlnfdfd아 이게아닌데..":
                
    return temp_list # 여기서 재귀를 써서 내보내야 할 것 같다.

row, column = map(int,input().split())
fire_list = list()
target = (-1,-1)
for i in range(row):
    fire_list.append(list(input()))
for i in range(row):
    for j in range(column):
        if fire_list[i][j] == '&':
            target = (i,j)
            print("target 설정 : ",target)
graph = dict()
print(graph)
temp_list = list()
root_graph(graph,temp_list,target,fire_list)

# 여기서 리스트로 들어온 각 요소를 하나하나 target으로 삼고 할 수 있나?
# 에이 그건 또 아니지;;;
# 인접한 위치에서의 리스트들을 다 구해주면 되는 건데
# 그게 말처럼 쉽지가 않아서.. 찾은건 인접 행렬과 인접 리스트..
def bfs(graph, start_node):
    visit = list()
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit

# print(bfs(graph,'A'))


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