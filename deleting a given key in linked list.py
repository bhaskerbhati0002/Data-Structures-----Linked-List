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
    def delete(self, value):
        tmp=self.start
        while (tmp.next.data != value):
            tmp=tmp.next
        tmp.next = tmp.next.next


    def display(self):
        tmp=self.start
        while(tmp!=None):
            print(tmp.data,end='->')
            tmp=tmp.next
        print("NULL")
list=ll()
list.create(5)
list.create(6)
list.create(7)
list.create(8)
list.display()
list.delete(7)
list.display()