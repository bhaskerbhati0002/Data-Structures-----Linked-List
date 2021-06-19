class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class ll():
    def __init__(self):
        self.start=None
    def beg(self):
        value=int(input('enter the data to join in beginning : '))
        newnode=node(value)
        if (self.start == None):
            self.start = newnode
        else:
            newnode.next=self.start
            self.start=newnode
    def end(self):
        value = int(input('enter the data to join in ending : '))
        newnode = node(value)
        if (self.start == None):
            self.start = newnode
        else:
            tmp=self.start
            while(tmp.next!=None):
                tmp=tmp.next
            tmp.next=newnode
    def place(self,place):
        if (place<=1):
            list.beg()
        tmp=self.start
        i=0
        while(tmp!=None):
            i=i+1
            tmp=tmp.next
        if(place>i):
            list.end()
        if(1<place<=i):
            tmp=self.start
            for j in range(1,place-1):
                tmp=tmp.next
            print('enter the data to be joined at',place,'place :',end=' ')
            value = int(input())
            newnode=node(value)
            newnode.next=tmp.next
            tmp.next=newnode
    def display(self):
        if(self.start==None):
            print('list is empty')
        else:
            tmp = self.start
            while (tmp != None):
                print(tmp.data, end='-->')
                tmp = tmp.next
list=ll()
print('1 for creation at the beginning\n2 for creation at the ending\n3 for creation at any place\n4 for display\n5 for EXIT')
n=int(input('enter the no. acc to task : '))
ch=0
if(n==5):
    print('EXITED!.........')
    ch=1
while(n!=5):

    if(n==1):
        list.beg()
    elif(n==2):
        list.end()
    elif(n==3):
        p=int(input('enter place to be entered : '))
        list.place(p)
    elif(n==4):
        list.display()
    else:
        print('not a valid input')
    n = int(input('\nenter the no. acc to task : '))
if(ch==0):
    print('EXITED!.........')