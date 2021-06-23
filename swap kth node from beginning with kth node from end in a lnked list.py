a=[]
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

    def swap(self,node):
        tmp=self.start
        ch=0
        while(tmp!=None):#counting the nodes in the linked list
            ch=ch+1
            tmp=tmp.next

        tmp=self.start#taking the kth node from beginning
        for i in range(1,node):
            tmp=tmp.next
        first=tmp

        tmp=self.start#taking the kth node from ending
        for i in range(1,ch-node+1):
            tmp=tmp.next
        second=tmp

        a=first.data#swapping (a is temporary variable for swapping)
        first.data=second.data
        second.data=a


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
list.display()
list.swap(3)
print(f"after swapping the given kth node.")
list.display()
