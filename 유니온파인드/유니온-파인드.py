par = [i for i in range(10000001)]
rank = [1 for _ in range(10000001)]

# find 함수
def _find(a):
    # 만약에 자식의 부모가 자식이라면
    if par[a] == a:
        # 맨 꼭대기에 있는 것이므로, return
        return a
    # 자식의 부모가 있다면
    else:
        # 모든 자식의 부모를 맨 꼭대기의 부모로 바꿔준다
        par[a] = _find(par[a])
        return par[a]

# union 함수
def _union(a,b):
    # 각각의 제일 상단 부모를 찾는다
    a = _find(a)
    b = _find(b)

    # 같은 부모라면
    if a == b:
        return

    # 더 짧은 트리로 더 긴 트리를 합친다.
    # 만약 두 부모가 동일 선상에 있으면,
    if rank[a] == rank[b]:
        # 합치고
        par[a] = b
        # b의 랭크를 올려준다 (합쳐졌으니까, 밑으로 붙는 구조) 노드의 랭크가 중요하다.
        rank[b] += 1
    # 밑에 자식이 더 많으면, b에 합쳐주고, 전체 깊이는 달라지지 않으므로,
    elif rank[a] > rank[b]:
        par[b] = a
    else:
        par[a] = b