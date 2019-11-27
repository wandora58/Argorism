
# 選択ソート
# 配列の中から「残っているもののうち一番小さいものを前に持って来る」を繰り返す

def select(array):

    for i in range(len(array)):
        s = i

        for j in range(i,len(array)):
            if array[s] > array[j]:
                s = j

        array[i],array[s] = array[s],array[i]

    return array



if __name__ == "__main__":

    array = [2,5,7,4,2,7,5,2,1]

    print(select(array))

# 計算量は O(n^2)
