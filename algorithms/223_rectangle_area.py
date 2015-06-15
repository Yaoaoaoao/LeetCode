class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        area1 = abs(A-C)*abs(D-B)
        area2 = abs(G-E)*abs(H-F)
        left, right, bottom, top = max(A,E), min(C,G), max(B,F), min(D,H)
        overlap = (right-left)*(top-bottom) if (left<=right and bottom<=top) else 0
        return area1+area2-overlap
    
print Solution().computeArea(0, 0, 0, 0, -1, -1, 1, 1) #4
print Solution().computeArea(-2, -2, 2, 2, -2, -2, 2, 2) #16