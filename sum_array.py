def sum(numbers):
    if not isinstance(numbers[0],list):
        if len(numbers) >= 2:
            return numbers[0]+sum(numbers[1:])
        else:
            return numbers[0]

    else:
        if len(numbers) >= 2:
            return sum(numbers[0])+sum(numbers[1:])
        else:
            return sum(numbers[0])


numbers = [
    [1, 2, 3, 4],
    [3, 6, [5, 6], 8, 2,[2, 4], 9],
    [4, 2, [6, 7, [2, 6, 1]]]
]
print("The sum is %s"%(sum(numbers)))
