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
    def counter(self,count):
        tmp=self.start
        ch=0
        while tmp!=None:
            if tmp.data==count:
                ch=ch+1
            tmp=tmp.next
        print(f"count of {count} is {ch} times.")

    def display(self):
        tmp=self.start
        while(tmp!=None):
            print(tmp.data,end='->')
            tmp=tmp.next
        print("NULL")

list=ll()
list.create(1)
list.create(2)
list.create(1)
list.create(2)
list.create(1)
list.create(3)
list.create(1)
list.display()
list.counter(1)
list.counter(2)
list.counter(3)