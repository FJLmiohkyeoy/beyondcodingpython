def binarySearch(target, data):
    if not data:
        return False

    mid = len(data)//2

    if data[mid] == target:
        return True
    elif data[mid] > target:
        return binarySearch(target, data[:mid])
    else:
        return binarySearch(target, data[mid+1:])


data = [i for i in range(10)]
print(binarySearch(7, data))
