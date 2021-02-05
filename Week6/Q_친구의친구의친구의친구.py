# 60점
# visited 배열로 푸는 것 같은데 ...


from collections import deque

def friends_dfs(edge_list,n,m):
    
    visited = [0] * n
    count = 0
    while edge_list:
        (a,b) = edge_list.popleft()
        if visited[a] == 0 and visited[b] == 0:
            visited[a] = 1
            count += 1
        if count == m:
            if visited[b] == 0:
                visited[b] = 1
    
    if sum(visited) == n:
        return 1
    else:
        return 0



if __name__ == "__main__":
    n,m = map(int,input().split())
    edge_list = deque()
    for _ in range(m):
        a,b = map(int,input().split())
        edge_list.append((a,b))
    print(friends_dfs(edge_list,n,m))