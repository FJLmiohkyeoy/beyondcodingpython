def permutation(arr, start):
    if (start == len(arr)):
        print("".join(arr))

    else:
        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start]
            permutation(arr, start+1)
            arr[i], arr[i] = arr[start], arr[i]


permutation([_ for _ in 'abc'], 0)
