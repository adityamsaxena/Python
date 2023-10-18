def Two_Sum(nums):
    target = 5
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                print([i,j])
Two_Sum([2,3,5,6,7])