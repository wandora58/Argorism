# coding=utf-8
class Node:
    def __init__(self, x, y=None):
        self.data = x  # データを格納
        self.next = y  # 次のノードを指し示すポインタを格納


class Linked_list:
    def __init__(self):
        self.top = None  # 空リストを作るために None で初期化

    # n番目に値xを挿入する関数
    def insert(self, n, x):
        if n == 0 or not self.top:  # 先頭(n=0)に値を挿入するか、リストが空配列なら
            self.top = Node(x, self.top)

        else:
            obj = self.top  # 先頭から順に連結リストを走査
            while obj.next:  # 該当位置 n に到達したら終了
                n -= 1
                if n == 0:
                    break
                obj = obj.next  # 次のノードに移動

            Newobj = Node(x, obj.next)  # Newobj → nノード
            obj.next = Newobj  # n-1ノード → Newobj
            # python は参照渡しより次のノードを next に渡して挙げるだけで良い

    # n番目のノードを削除するメソッド
    def delete(self, n):
        if n == 0:
            if self.top:  # 連結リストが空配列でなければ
                self.top = self.top.next  # self.top が指し示すノードを1個後ろのノードにずらす
                return True  # 削除ができたら True を返す

        else:
            obj = self.top  # 先頭から順に連結リストを走査
            while obj.next:  # 該当位置 n に到達したら終了
                n -= 1
                if n == 0:
                    obj.next = obj.next.next  # obj.next が指し示すノードを1個後ろのノードにずらす
                    return True  # 削除ができたら True を返す
                obj = obj.next  # 次のノードに移動

        return False

    # 値 x のノードの位置を探索するメソッド
    def index(self, x):
        n = 0
        obj = self.top  # 先頭から順に連結リストを走査
        while obj:
            if obj.data == x:  # 値 x に該当するデータがあったら n を返す
                return n
            n += 1
            obj = obj.next
        return -1

    def show(self):
        n = 0
        obj = self.top
        linklist = []

        while obj:
            linklist.append(obj.data)
            obj = obj.next

        return linklist


if __name__ == "__main__":

    linklist = Linked_list()

    for i in range(5):
        linklist.insert(i, i ** 2)

    print(linklist.index(9))

    print(linklist.show())
    linklist.delete(linklist.index(9))
    print(linklist.show())
