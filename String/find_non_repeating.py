
# 文字列が与えられると、最初に反復していない文字を見つけます
# 文字列が与えられたら、その中の最初の非反復文字を見つけます。
# たとえば、入力文字列が「GeeksforGeeks」の場合、出力は「f」であり、入力文字列が「GeeksQuiz」の場合、出力は「G」です。
# ないなら「-1」をし出力

def find_non_repeating(string):

    count = [0] * 256
    for i in string:
        count[ord(i)] += 1

    index = -1
    k = 0

    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1

    return index


if __name__ == "__main__":
    s = input()

    print(find_non_repeating(s))
