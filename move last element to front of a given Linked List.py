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

    def movetofront(self):
        tmp=self.start
        while tmp.next.next!=None:
            tmp=tmp.next
        pre=tmp
        new_head=tmp.next
        pre.next=None
        new_head.next=self.start
        self.start=new_head

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
list.display()
list.movetofront()
list.display()
list.create(6)
list.display()