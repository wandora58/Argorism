
# 二つの文字列を並び替えて一致するか

import collections

if __name__ == "__main__":

    s1 = [3,5,2,5,2]
    s2 = [2,3,5,5,2]

    dic_s1 = collections.Counter(s1)
    dic_s2 = collections.Counter(s2)

    flag = 0
    for key in dic_s1:
        if dic_s1[key] != dic_s2[key]:
            flag = 1

    if flag == 0:
        print('True')
    else:
        print('False')
