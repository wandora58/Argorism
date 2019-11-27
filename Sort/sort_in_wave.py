
# 整数の並べ替えられていない配列を指定すると、配列を配列のような波に並べ替えます。
# 配列「arr[0..n-1]」は、arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4]> = …の場合、波形でソートされます。

# 考え方はすべての偶数位置（インデックス0、2、4、..）の要素が、
# 隣接する奇数要素よりも大きいことを確認すれば奇数位置の要素を心配する必要がない

def wave_sort(array):

    i = 0
    while True:

        if i == 0:
            if array[0] < array[1]:
                array[0],array[1] = array[1],array[0]

        if i >= len(array)-2:
            if array[-1] < array[-2]:
                array[-1],array[-2] = array[-2],array[-1]
            break

        if array[i-1] > array[i]:
            array[i-1],array[i] = array[i],array[i-1]

        if array[i+1] > array[i]:
            array[i+1],array[i] = array[i],array[i+1]

        i += 2

    return array

if __name__ == "__main__":

    array = [10, 5, 6, 3, 2, 20, 100, 80]
    print(wave_sort(array))
