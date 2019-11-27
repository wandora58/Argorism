

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.top = None


    def insert(self, n, data):
        if n == 0 or self.top is None:
            self.top = Node(data,self.top)

        else:
            obj = self.top
            while obj:
                n -= 1
                if n == 0:
                    Newobj = Node(data,obj.next)
                    obj.next = Newobj
                    return

                obj = obj.next

                if obj is None:
                    print("Cannot insert")
                    return


    def delete(self, n):
        if self.top is None:
            print("Cannot delete")
            return

        elif n == 0:
            self.top = self.top.next

        else:
            obj = self.top
            while obj:
                n -= 1
                if n == 0:
                    obj.next = obj.next.next
                    return

                obj = obj.next

                if obj is None:
                    print("Cannot delete")
                    return


    def index(self, data):
        obj = self.top
        n = 0
        while obj:
            if obj.data == data:
                return n
            n += 1
            obj = obj.next

        return "Not Found"


    def show(self):
        obj = self.top
        res = []

        while obj:
            res.append(obj.data)
            obj = obj.next

        return res
        

if __name__ == "__main__":

    lst = Linkedlist()

    for i in range(5):
        lst.insert(i,i**2)

    print(lst.index(9))
    print(lst.show())
    lst.delete(2)
    print(lst.show())
