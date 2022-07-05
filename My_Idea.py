class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:

        required_steps = abs(target[0]) + abs(target[1])

        for ghost in ghosts:

            steps = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])

            if steps <= required_steps:
                return False

        return True