def search(nums, target):
    index = -1

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            index = mid
            break
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return index


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    print(search(nums, target))
    target = 9
    print(search(nums, target))
