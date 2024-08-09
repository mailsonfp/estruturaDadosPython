def maximumCount(nums):
    positive = 0
    negative = 0

    for i in range(len(nums)):
        if nums[i] < 0:
            negative += 1
        elif nums[i] > 0:
            positive += 1

    return max(negative, positive)


if __name__ == '__main__':
    nums = [-2, -1, -1, 1, 2, 3]
    print(maximumCount(nums))

    nums = [-3, -2, -1, 0, 0, 1, 2]
    print(maximumCount(nums))

    nums = [5, 20, 66, 1314]
    print(maximumCount(nums))



