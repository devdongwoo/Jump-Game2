""" 
# my solution
def jumpGame(nums):
    visited = []
    n = 0
    transPoint = False
    def dfs(idx):
        nonlocal n, transPoint
            

        if idx == len(nums)-1:
            return
            
        for i in range(nums[idx]+1):
            if i != 0 and i+idx < len(nums) and nums[i+idx] != 0:
                transPoint = False
                n += 1
                    

                if idx+i == len(nums)-1:
                    transPoint = True
                    visited.append(n)
                    
                    
                dfs(i+idx)
                if transPoint is True:
                    n -= 1
    dfs(0)
    if len(nums) <= 1:
        return 0
    visited.sort()
    return visited[0]


print(jumpGame([5,9,3,2,1,0,2,3,3,1,0,1]))
 """


#other person solution
def jump(nums):
    res = 0
    l = r = 0

    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r+1):
            farthest =  max(farthest, i + nums[i])
        
        l = r+1
        r = farthest
        res += 1
    return res
print(jump([2,3,1,1,4]))