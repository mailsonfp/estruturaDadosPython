def remove_duplicates(nums_param):
    point_one = 0
    point_two = 1
    counter_duplicated = 0
    for i in range(len(nums_param)):
        print(f'i: {i}')
        print(f'point_one: {point_one}')
        print(f'point_two: {point_two}')
        print(f'array_size: {len(nums_param)}')
        print(f'array: {nums_param}')
        print(f'array[point_one]: {nums_param[point_one]}')
        print(f'array[point_two]: {nums_param[point_two]}')

        if nums_param[point_one] == nums_param[point_two]:
            del nums_param[point_two]
            counter_duplicated += 1
        else:
            point_one += 1
            point_two += 1

        if point_one == len(nums) or point_two == len(nums) - 1:
            break

    return counter_duplicated


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
