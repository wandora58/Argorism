
# ugly number は、素因数が2、3、5のみの数字です。
# シーケンス1、2、3、4、5、6、8、9、10、12、15、…は最初の11個の ugly number を示します。慣例により、1が含まれます。
#
# 番号 n を指定して n番目の ugly number を見つけなさい

# n を 2か3か5でそれぞれ割れるとこまで割る
def max_division(n,i):

    while n % i == 0:
        n //= i

    return n

# ugly number か判定するメソッド
def is_ugly(n):

    n = max_division(n,2)
    n = max_division(n,3)
    n = max_division(n,5)

    if n == 1:
        return True
    else:
        return False


def ugly_number(n):

    # ugly number を格納するリスト
    ugly_number = [1]

    count = 1
    i = 1

    while count <= n:

        i += 1

        if is_ugly(i):
            count += 1
            ugly_number.append(i)


    return ugly_number[n-1]


if __name__ == "__main__":

    n = int(input())
    print(ugly_number(n))
