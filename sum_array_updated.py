def sum(numbers):
    total = 0
    for num in numbers:
        if type(num) is int:
            total+=num
        else:
            total+=sum(num)
    return total


numbers = [
    [1, 2, 3, 4],
    [3, 6, [5, 6], 8, 2,[2, 4], 9],
    [4, 2, [6, 7, [2, 6, 1]]]
]
print("The sum is %s"%(sum(numbers)))
