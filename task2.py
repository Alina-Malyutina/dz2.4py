def dictionary(one, two):
    dictum = {
        f'{one}': id(one),
        f'{two}': id(two)
    }

    return dictum


a = 4
b = 8
temp = dictionary(a, b)
print(temp)
