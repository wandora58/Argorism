
# 2つのリンクリストの交点を取得する関数を作成します
# 単一リンクのリストが2つあります
# リンクリストの1つのエンドノードが2番目のリストにリンクされ、逆Y字型リストが形成されました
# 2つのリンクリストがマージされるポイントを取得するプログラムを作成しなさい

class Node:
    def __init__(self, x, y=None):
        self.data = x
        self.next = y

class linkedlist:
    def __init__(self):
        self.top = None

    def insert(self, n, x):
        if n == 0 or self.top is None:
            self.top = Node(x, self.top)

        else:
            node = self.top

            while node.next:
                n -= 1
                if n == 0:
                    break
                node = node.next

            node.next = Node(x,node.next)

    def show(self):
        obj = self.top
        linklist = []

        while obj:
            linklist.append(obj.data)
            obj = obj.next

        return linklist

# アドレスをみて取得
def intersection_point(lst1,lst2):
    obj1 = lst1.top
    obj1_adress = []

    while obj1:
        obj1_adress.append(obj1)
        obj1 = obj1.next

    obj2 = lst2.top
    obj2_adress = []

    while obj2:
        obj2_adress.append(obj2)
        obj2 = obj2.next

    i = 0
    while True:
        if obj1_adress[i] == obj2_adress[i]




if __name__ == "__main__":
    linklist1 = linkedlist()
    linklist2 = linkedlist()

    linklist1.insert(0,3)
    linklist1.insert(1,6)
    linklist1.insert(2,9)
    linklist1.insert(3,15)
    linklist1.insert(4,30)

    linklist2.insert(0,10)
    linklist2.insert(1,15)
    linklist2.insert(2,30)

    print(linklist1.show())
    print(linklist2.show())
