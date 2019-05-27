# _*_coding:utf-8_*_
# __author: a123456
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> [[int]]:
        positions = []
        for r in range(R):
            for c in range(C):
                positions.append([r, c])

        def compare(position: []):
            r, c = position
            return abs(r0 - r) + abs(c0 - c)

        return sorted(positions, key=compare)


if __name__ == '__main__':
    s = Solution()
    print(s.allCellsDistOrder(2, 2, 0, 1))
