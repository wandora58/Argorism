

def mergesort(array):

    mid = len(array)

    if mid > 1:
        left = mergesort(array[:mid//2])
        right = mergesort(array[mid//2:])

        array = []

        while True:

            if left[0] <= right[0]:
                array.append(left.pop(0))

                if len(left) == 0:
                    array.extend(right)
                    break

            if right[0] < left[0]:
                array.append(right.pop(0))

                if len(right) == 0:
                    array.extend(left)
                    break

    return array


def quiksort(array):

    if len(array) < 2:
        return array

    pivot = array[0]

    left = []
    right = []
    count = 0

    for i in array:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            count += 1

    return quiksort(left) + [pivot]*count + quiksort(right)


if __name__ == "__main__":

    array = [3,2,4,2,7,4,5,7]
    print(mergesort(array))
    print(quiksort(array))
