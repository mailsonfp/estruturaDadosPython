def find_repetead_number(nums, target):
    exits_repetead_number = False

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            exits_repetead_number = True
            break
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return exits_repetead_number

# for i in range(len(array)):
#    exits_repetead_number = find_repetead_number(array[i+1:len(array)], i)
#    if exits_repetead_number:
#        break

# return exits_repetead_number