class LinearQueue:
    
    def __init__(self,size):
        self.size=size
        self.list1=[0 for i in range(size)]
        self.front=-1
        self.rear=-1
    def insertion(self,item):
        # self.item=item
        if self.rear==self.size-1:
            print("Queuen is Full")
            return 0
        else:
            
            self.rear=self.rear + 1
            self.list1[self.rear]=item
            if self.front==-1:
                self.front=0
            print("List of the Queue: ",self.list1)
    def traverse(self):
        if self.rear==self.front==-1:
            print("Queue is Empty")
        else:
            print("Queue in list is ",self.list1)
    def deletion(self):
        if self.front==self.rear==-1:
            print("Queue is Empty")
            return 0
        item=self.list1[self.front]
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=self.front+1
        return item
                
            
            
s=LinearQueue(4)
s.insertion(12)
s.insertion(22)
s.insertion(15)
print("Deletion of an Element: ",s.deletion())
s.insertion(14)
print("Deletion of an Element: ",s.deletion())
print("Deletion of an Element: ",s.deletion())
print("Deletion of an Element: ",s.deletion())
