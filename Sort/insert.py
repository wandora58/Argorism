

if __name__ == "__main__":

    a = [4,1,5,3,2]

    for i in range(1,len(a)):
        tmp = a[i]

        if tmp < a[i-1]:
            j = i

            while True:
                a[j] = a[j-1]
                j -= 1

                if j == 0 or tmp >= a[j-1]:
                    break
            a[j] = tmp


    print(a)
