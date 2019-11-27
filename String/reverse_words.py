
# 指定された文字列の単語を逆順にする
# ex ) i like soccer very much → much very soccer like i

def reverse_string(s):

    words = s.split()
    string = []
    for word in words:
        string.insert(0,word)

    return ' '.join(string)


if __name__ == "__main__":

    s = "i like this program very much"
    print(reverse_string(s))
