
# DFS

# 시작 정점 v를 결정하여 방문
# 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문
# w를 v로하여 다시 반복

# 방문하지 않는 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로하여 다시 반복


graph = [
    [], # 0
    [2,3,8], # 1이랑 연결된 2,3,8
    [1,7], # 2랑 연결된 1,7
    [1,4,5], # 3이랑 연결된
    [3,5], # 4랑 연결된
    [3,4], # 5랑 연결된
    [7], # 6
    [2,6,8], # 7
    [1,7] # 8
]

visited = [False]
def DFS(graph,v):
    visited = []
    stack = [v]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack_e = list(graph[n])
            stack_e.sort(reverse=True)
            stack += list(graph[n])
    return visited