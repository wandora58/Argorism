# MS Excelの列には、A、B、C、…、Z、AA、AB、ACなどのパターンがあります。
# 列1は「A」、列2は「B」、列27は「AA」と命名されます。
# 列番号を指定して、対応するExcel列名を見つけます。以下に例を示します。
#
# input          output
# 26             Z
# 51             AY


def excelcolumn(n):
    column = []

    while n > 0:
        rem = n % 26  # 余り

        if rem == 0:
            column.insert(0, 'Z')
            n = (n // 26) - 1

        else:
            column.insert(0, chr(rem + 64))
            n //= 26

    return ''.join(column)


if __name__ == "__main__":
    n = int(input())

    print(excelcolumn(n))
