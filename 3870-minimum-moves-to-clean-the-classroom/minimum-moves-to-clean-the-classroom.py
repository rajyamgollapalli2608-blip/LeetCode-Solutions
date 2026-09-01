from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        # Give each litter an index
        litter = {}
        start = None

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        total_litter = len(litter)

        # All litter collected
        target = (1 << total_litter) - 1

        # BFS state: row, col, remaining_energy, mask
        q = deque()
        q.append((start[0], start[1], energy, 0))

        visited = set()
        visited.add((start[0], start[1], energy, 0))

        moves = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                if mask == target:
                    return moves

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Outside grid
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    # Wall
                    if classroom[nr][nc] == 'X':
                        continue

                    # No energy
                    if e == 0:
                        continue

                    ne = e - 1
                    nmask = mask

                    # Litter
                    if classroom[nr][nc] == 'L':
                        idx = litter[(nr, nc)]
                        nmask |= (1 << idx)

                    # Recharge
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    state = (nr, nc, ne, nmask)

                    if state not in visited:
                        visited.add(state)
                        q.append(state)

            moves += 1

        return -1