def countNegatives(nums):
    if nums[len(nums) - 1] < 0:
        return len(nums)
    elif nums[0] >= 0:
        return 0

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < 0 <= nums[mid + 1]:
            break
        elif nums[mid] < 0:
            left = mid + 1
        else:
            right = mid - 1

    return mid + 1


def countPositives(nums):
    if nums[0] > 0:
        return len(nums)
    if nums[len(nums) - 1] <= 0:
        return 0

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > 0 >= nums[mid + 1]:
            break
        elif nums[mid] > 0:
            right = mid - 1
        else:
            left = mid + 1

    return len(nums) - mid


def maximumCount(nums):
    positive = countPositives(nums)
    # print(positive)
    negative = countNegatives(nums)
    # print(negative)

    return max(negative, positive)


if __name__ == '__main__':
    nums = [-2, -1, -1, 1, 2, 3]
    print(maximumCount(nums))

    nums = [-3, -2, -1, 0, 0, 1, 2]
    print(maximumCount(nums))

    nums = [5, 20, 66, 1314]
    print(maximumCount(nums))
