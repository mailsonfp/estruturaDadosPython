def maximumCount(nums):
    negatives, positives = len(nums), len(nums)

    for i in range(len(nums)):
        if nums[i] >= 0:
            negatives = i
            break

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] <= 0:
            positives = len(nums) - 1 - i
            break

    return max(negatives, positives)


if __name__ == '__main__':
    nums = [-2,-1,-1,1,2,3]
    print(maximumCount(nums))

    nums = [-3, -2, -1, 0, 0, 1, 2]
    print(maximumCount(nums))

    nums = [5, 20, 66, 1314]
    print(maximumCount(nums))



