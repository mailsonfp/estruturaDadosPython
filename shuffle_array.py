def shuffle(nums, n):
    retorno = [0] * (n * 2)

    right = n
    left = 0

    i = 0
    while right < len(retorno):
        retorno[i] = nums[left]
        retorno[i + 1] = nums[right]

        left += 1
        right += 1
        i += 2

    return retorno


if __name__ == '__main__':
    nums = [2,5,1,3,4,7]
    n = 3

    print(shuffle(nums, n))