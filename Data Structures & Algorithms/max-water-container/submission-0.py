class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        lp = 0
        rp = len(heights) - 1

        max_area = 0
        while lp < rp:

            max_height = 0

            width = rp - lp
            print(width)
            print(min(heights[lp],  heights[rp]))
            current_area = min(heights[lp],  heights[rp]) * width
            max_area = max(current_area, max_area)

            print(max_area)
            if heights[lp] <= heights[rp]:
                lp += 1
            else: 
                rp -= 1


        return max_area