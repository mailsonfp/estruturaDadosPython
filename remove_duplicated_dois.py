def remove_duplicates(nums):
    # counter = {}
    # for n in nums:
    #  counter[n] = counter.get(n, 0) + 1
    # k = 0
    if len(nums) == 0:
        return 0

    left, right = 0, 1
    index = 0

    for i in range(1, len(nums)):
        if nums[index] != nums[i]:
            index += 1
            nums[index] = nums[i]

    print(nums)
    return index + 1


if __name__ == '__main__':
    print('Primeira execução:' + '-' * 20)
    nums = [1, 1, 2]
    print(remove_duplicates(nums))
    print(nums)

    print('-' * 20)
    print('-' * 20)
    print('-' * 20)

    print('Segunda execução:' + '-' * 20)
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(remove_duplicates(nums))
    print(nums)
