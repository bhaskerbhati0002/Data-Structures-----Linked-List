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
    def middle(self):
        tmp=self.start
        ch=0
        while (tmp!=None):
            tmp=tmp.next
            ch=ch+1
        tmp=self.start
        if ch%2==0:
            for i in range(ch//2):
                tmp=tmp.next
            return tmp.data
        else:
            for i in range(ch//2):
                tmp = tmp.next
            return tmp.data


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
list.create(4)
list.create(5)
list.create(6)
list.create(7)
list.create(8)
list.create(9)
list.display()
print(f"middle is {list.middle()}")
list.create(10)
list.display()
print(f"middle is {list.middle()}")