user_input = input().upper()


def sol(user_input):
    obj = {}
    maxNumber = 0
    result = ""

    for i in user_input:
        if i in obj:
            obj[i] += 1
        else:
            obj[i] = 1

    for key in obj:
        if obj[key] > maxNumber:
            maxNumber = obj[key]
            result = key
        elif obj[key] == maxNumber:
            result = "?"

    return result


print(sol(user_input))
