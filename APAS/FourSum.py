nums = [1, -2, -5, -4, -3, 3, 3, 5]
nums.sort()
target = -11
ans = []
for i in range(len(nums)-3):
    if i > 0:
        if nums[i] == nums[i-1]:
            continue
    for j in range(i+1, len(nums)-2):
        if j > i+1:
            if nums[j] == nums[j-1]:
                continue
        low = j+1
        high = len(nums)-1
        while low < high:
            if low > j+1:
                if nums[low] == nums[low-1]:
                    low += 1
                    continue
            if high < len(nums)-1:
                if nums[high] == nums[high+1]:
                    high -= 1
                    continue
            temp = nums[i]+nums[j]+nums[low]+nums[high]-target
            print(nums[i], nums[j], nums[low], nums[high], "=", temp)
            if temp == 0:
                ans.append([nums[i], nums[j], nums[low], nums[high]])
                low += 1
                high -= 1
            elif temp > 0:
                high -= 1
            else:
                low += 1
print(ans)
