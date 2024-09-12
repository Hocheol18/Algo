# 수민 풀이 ;

from collections import deque

def solution(maze):
    # 최대 4*4칸
    n, m = len(maze), len(maze[0])
    answer = 0

    # 시작점과 끝점 찾기
    r_start, b_start, r_end, b_end = None, None, None, None
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                r_start = (i, j)
            elif maze[i][j] == 2:
                b_start = (i, j)
            elif maze[i][j] == 3:
                r_end = (i, j)
            elif maze[i][j] == 4:
                b_end = (i, j)

    # BFS를 위한 큐 초기화 - 수레의 현재위치, 방문기록, 턴수, 각 수레의 도착점 방문 여부
    queue = deque([(r_start, b_start, set([r_start]), set([b_start]), 0, False, False)])

    # 이동 방향
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        r_pos, b_pos, r_visited, b_visited, turns, r_done, b_done = queue.popleft()

        # 두 수레 모두 도착했는지 확인 - answer 갱신 조건
        if r_done and b_done:
            if answer == 0:
                answer = turns
            else:
                answer = min(answer, turns)
            continue

            # 모든 가능한 이동 조합 확인
        # 두 수레 중 도착한 수레는 이번 턴에 이동하지 않기에 (0, 0) 반환
        for r_dir in directions if not r_done else [(0, 0)]:
            for b_dir in directions if not b_done else [(0, 0)]:
                # 빨간 수레가 도착점에 도착한 상태라면 도착점을 유지 - 그렇지 않다면 새로운 위치로 이동
                new_r_pos = (r_pos[0] + r_dir[0], r_pos[1] + r_dir[1]) if not r_done else r_pos
                # 파란 수레가 도착점에 도착한 상태라면 도착점을 유지
                new_b_pos = (b_pos[0] + b_dir[0], b_pos[1] + b_dir[1]) if not b_done else b_pos

                # 이미 도착했거나 이번 턴에 도착했는지 확인
                new_r_done = r_done or new_r_pos == r_end
                new_b_done = b_done or new_b_pos == b_end

                # 이동이 유효한지 확인 - 일단 이동하고 유효성을 검사한다.
                # 두 수레의 위치가 유효(도착 상태도 포함)하고 같은 위치로 이동하는 것이 아니고, 두 수레가 위치를 바꿔 이동하는 것이 아니라면
                if ((is_valid_move(maze, new_r_pos, r_visited) or new_r_done) and
                        (is_valid_move(maze, new_b_pos, b_visited) or new_b_done) and
                        new_r_pos != new_b_pos and
                        (r_pos, b_pos) != (new_b_pos, new_r_pos)):

                    # 이번 경로의 방문기록을 전달 
                    new_r_visited = r_visited.copy()
                    new_b_visited = b_visited.copy()
                    if not new_r_done:  # 이번 턴에도 아직 도착지에 도착하지 않았다면 새로운 위치를 방문 처리
                        new_r_visited.add(new_r_pos)
                    if not new_b_done:
                        new_b_visited.add(new_b_pos)
                    # 턴 수를 증가 + 수레의 위치 이동 + 방문 처리된 상태로 다음 턴으로 이동 : 유효한 판의 상태만 큐에 들어간다.
                    queue.append(
                        (new_r_pos, new_b_pos, new_r_visited, new_b_visited, turns + 1, new_r_done, new_b_done))

    # 큐가 비었는데도 answer가 갱신되지 않았다면 = 두 수레 중 하나라도 도착점에 도착할 수 없는 경우라면, 0을 반환
    return answer


# 여기서는 이동할 위치가 범위 내에 있는지와 벽이 아닌지, 방문한 적이 없는지만 체크한다.
def is_valid_move(maze, pos, visited):
    n, m = len(maze), len(maze[0])
    return (0 <= pos[0] < n and 0 <= pos[1] < m and
            maze[pos[0]][pos[1]] != 5 and
            pos not in visited)