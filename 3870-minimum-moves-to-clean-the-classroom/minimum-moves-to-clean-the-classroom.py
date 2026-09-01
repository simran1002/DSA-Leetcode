from collections import deque, defaultdict
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        ROW = len(classroom)
        COL = len(classroom[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        start = (-1, -1)
        litter_map = {}
        litter_count = 0
        
        for r in range(ROW):
            for c in range(COL):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_map[(r, c)] = litter_count
                    litter_count += 1
                    
        target_mask = (1 << litter_count) - 1
        
        queue = deque([(start[0], start[1], 0, 0, energy)])
        
        best_energy = [[defaultdict(lambda: -1) for _ in range(COL)] for _ in range(ROW)]
        best_energy[start[0]][start[1]][0] = energy
        
        while queue:
            r, c, mask, moves, curr_energy = queue.popleft()
            
            if mask == target_mask:
                return moves
                
            if curr_energy == 0 and classroom[r][c] != 'R':
                continue
                
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                
                if not (0 <= nr < ROW and 0 <= nc < COL):
                    continue
                if classroom[nr][nc] == 'X':
                    continue
                    
                new_mask = mask
                if classroom[nr][nc] == 'L':
                    bit_idx = litter_map[(nr, nc)]
                    new_mask |= (1 << bit_idx)
                    
                if classroom[nr][nc] == 'R':
                    new_energy = energy
                else:
                    base_energy = energy if classroom[r][c] == 'R' else curr_energy
                    new_energy = base_energy - 1
                    
                if new_energy < 0:
                    continue
                    
                if best_energy[nr][nc][new_mask] < new_energy:
                    best_energy[nr][nc][new_mask] = new_energy
                    queue.append((nr, nc, new_mask, moves + 1, new_energy))
                    
        return -1