class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        nr, nc = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()
        result =[]
        
        def dfs(r, c, o):

            dirr = [(0,1), (0,-1), (1,0), (-1,0)]
            o.add((r, c))

            for dr, dc in dirr:
                if r+dr >= 0 and r+dr < nr and c+dc >= 0 and c+dc < nc and heights[r][c] <= heights[r+dr][c+dc] and (r+dr, c+dc) not in o:
                    dfs(r+dr, c+dc, o)
        

        for i in range(nr):
            dfs(i, 0, pacific)
            dfs (i, nc-1, atlantic)
        
        for i in range(nc):
            dfs(0, i, pacific)
            dfs(nr-1, i, atlantic)

        print(pacific)
        print(atlantic)

        for r , c in pacific:
            if (r,c) in atlantic:
                result.append([r,c])

        return result



        
        