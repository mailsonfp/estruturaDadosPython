def reverse_string(s):
    left, right = 0, len(s) - 1

    retorno = ""

    while left < right:
        aux = s[right]

        s[right] = s[left]
        s[left] = aux

        left += 1
        right -= 1

    return s


if __name__ == '__main__':
    word = "Renaissance"
    print(reverse_string(word))

