a=[]
b=[]

class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.start=None
    def create(self,value):
        newnode=node(value)
        if(self.start==None):
            self.start = newnode
        else:
            tmp=self.start
            while (tmp.next != None):
                tmp = tmp.next
            tmp.next = newnode
    def counter(self):
        tmp=self.start
        while tmp!=None:
            a.append(tmp.data)
            tmp=tmp.next

        for i in range(len(a)-1,-1,-1):
            b.append(a[i])
        if a==b:
            print("True, is palindrome.")
        else:
            print("False, is not palindrome.")

    def display(self):
        tmp=self.start
        while(tmp!=None):
            print(tmp.data,end='->')
            tmp=tmp.next
        print("NULL")

list=ll()
list.create(1)
list.create(2)
list.create(3)
list.create(3)
list.create(2)
list.create(1)
list.display()
list.counter()
list.create(5)
list.display()
list.counter()