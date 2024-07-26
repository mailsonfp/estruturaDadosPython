def count_pairs(nums, target):
    count = 0
    nums.sort()
    for i in range(len(nums)):
        if nums[i] + nums[len(nums)-1] < target:
            count += (len(nums) - i) - 1

        left = i + 1
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[i] + nums[mid] >= target > nums[i] + nums[mid - 1]:
                count += ((mid - 1) - (i + 1) + 1)
                break
            elif nums[i] + nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

    return count


if __name__ == '__main__':
    nums = [-6, 2, 5, -2, -7, -1, 3]
    target = -2
    print(count_pairs(nums, target))

    nums = [-1, 1, 2, 3, 1]
    target = 2
    print(count_pairs(nums, target))
