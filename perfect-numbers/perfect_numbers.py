def classify(number):
    if number < 1:
        raise ValueError("Positive Numbers Only")

    aliquotSum = 1
    i = 2

    while i**2 < number:
        if not number % i:
            aliquotSum += i + number/i
        i += 1

    if aliquotSum == number and aliquotSum != 1:
        return "perfect"
    if aliquotSum > number:
        return "abundant"
    return "deficient"
