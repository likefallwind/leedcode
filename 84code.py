class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        columnNo = len(heights)
        if columnNo == 0:
            return 0
        leftStack = [0]
        leftLoc = [0] * columnNo
        for i, height in enumerate(heights[1:], start = 1):
            while(len(leftStack) > 0):
                bigLoc = leftStack[-1]
                bigNumber = heights[bigLoc]
                if height > bigNumber:
                    leftStack.append(i)
                    leftLoc[i] = bigLoc + 1
                    break
                else:
                    leftStack.pop()
            if(len(leftStack) == 0):
                leftStack.append(i)
                leftLoc[i] = 0
        rightStack = [columnNo - 1]
        rightLoc = [columnNo - 1] * columnNo
        for i in range(1, columnNo):
            nowLoc = columnNo - i - 1
            height = heights[nowLoc]
            while(len(rightStack) > 0):
                bigLoc = rightStack[-1]
                bigNumber = heights[bigLoc]
                if height > bigNumber:
                    rightStack.append(nowLoc)
                    rightLoc[nowLoc] = bigLoc - 1
                    break
                else:
                    rightStack.pop()
            if len(rightStack) == 0:
                rightStack.append(nowLoc)
                rightLoc[nowLoc] = columnNo - 1
        maxArea = 0
        for i in range(columnNo):
            leftNo = leftLoc[i]
            rightNo = rightLoc[i]
            thisArea = heights[i] * (rightNo - leftNo + 1)
            maxArea = max(maxArea, thisArea)
        return maxArea

            
            
        