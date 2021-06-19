a=[]
b = []
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

    def delete(self):
        if (self.start == None):
            print('list is empty')
        else:
            self.start = self.start.next

    def remove(self):
        tmp=self.start

        #adding linked to list to array a
        while tmp!=None:
            a.append(tmp.data)
            tmp=tmp.next

        #adding non duplicated list to array b
        for i in a:
            if i not in b:
                b.append(i)

        #deleting the previous linked list
        for i in range(len(a)):
            list.delete()

        #creating the new linked list with array b
        for j in range(len(b)):
            list.create(b[j])

    def display(self):
        tmp=self.start
        while(tmp!=None):
            print(tmp.data,end='->')
            tmp=tmp.next
        print("NULL")
list=ll()
list.create(9)
list.create(1)
list.create(2)
list.create(3)
list.create(4)
list.create(4)
list.create(5)
list.create(6)
list.create(6)
list.create(7)
list.create(8)
list.create(8)
list.create(9)
list.create(10)
list.display()
list.remove()
list.display()