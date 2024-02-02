def pair_sum(ar, k):
    if len(ar) < 2:
        return "Two small for sum"

    seen = set()
    output = set()

    for num in ar:
        target = k - num
        if target in seen:
            output.add((min(num, target), max(num, target)))
        seen.add(num)
    print('\n'.join(map(str, list(output))))


pair_sum([1, 3, 2, 2], 4)
