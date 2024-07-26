def count_pairs(nums, target):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] < target:
                count += 1

    return count


if __name__ == '__main__':
    nums = [-6, 2, 5, -2, -7, -1, 3]
    target = -2
    print(count_pairs(nums, target))

    nums = [-1, 1, 2, 3, 1]
    target = 2
    print(count_pairs(nums, target))
