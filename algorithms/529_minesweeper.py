class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        board = [list(b) for b in board]
        x, y = click
        lx, ly = len(board), len(board[0])

        def neighbor_mine(a, b):
            n = []
            # top
            if a > 0:
                if b > 0:  n.append((a - 1, b - 1))
                n.append((a - 1, b))
                if b < ly - 1: n.append((a - 1, b + 1))
            # center
            if b > 0:  n.append((a, b - 1))
            if b < ly - 1:  n.append((a, b + 1))
            # bottom
            if a < lx - 1:
                if b > 0:  n.append((a + 1, b - 1))
                n.append((a + 1, b))
                if b < ly - 1: n.append((a + 1, b + 1))
            return n

        def count_mine(lst):
            return sum([1 if board[a][b] == 'M' else 0 for a, b in lst])

        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:  # 'E'
            stack = [(x, y)]
            while len(stack) > 0:
                cx, cy = stack.pop(0)
                if board[cx][cy] == 'M':
                    continue
                elif board[cx][cy] == 'E':
                    neighbor = neighbor_mine(cx, cy)
                    count = count_mine(neighbor)
                    if count > 0:
                        board[cx][cy] = str(count)
                    else:
                        board[cx][cy] = 'B'
                        stack.extend(neighbor)
                else:  # already checked
                    continue

        return [''.join(b) for b in board]


# print Solution().updateBoard([['E', 'E', 'E', 'E', 'E'],
#                               ['E', 'E', 'M', 'E', 'E'],
#                               ['E', 'E', 'E', 'E', 'E'],
#                               ['E', 'E', 'E', 'E', 'E']], [3, 0])
# print Solution().updateBoard([['B', '1', 'E', '1', 'B'],
#                               ['B', '1', 'M', '1', 'B'],
#                               ['B', '1', '1', '1', 'B'],
#                               ['B', 'B', 'B', 'B', 'B']], [1, 2])
# print Solution().updateBoard(["EEEEE","EEMEE","EEEEE","EEEEE"],[3,0])
# print Solution().updateBoard(["BBBBBB1E","B111BB1M","12M1BB11","M211BBBB",
# "11BBBBBB","BBBBBBBB","B1221BBB","B1MM1BBB"], [0,7])
# ["BBBBBB11","B111BB1M","12M1BB11","M211BBBB","11BBBBBB","BBBBBBBB",
# "B1221BBB","B1MM1BBB"]
print Solution().updateBoard(
    ["EMM2BBBB", "EEM2BBBB", "EE21BBBB", "EM1BBBBB", "1221BBBB", "B1M1BBBB",
     "B111BBBB", "BBBBBBBB"], [0, 0])
# ["1MM2BBBB","EEM2BBBB","EE21BBBB","EM1BBBBB","1221BBBB","B1M1BBBB",
# "B111BBBB","BBBBBBBB"]
