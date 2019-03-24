class Node:
    def __init__(self,val):
        self.value=val
        self.next=None

class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node
        print(self.head)
        return self
    def print_value(self):
        runner=self.head
        while(runner!=None):
            print(runner.value)
            runner=runner.next
        return self
    def add_to_back(self, val):
        new_node=Node(val)
        runner=self.head
        if(runner==None):
            self.add_to_front(val)
            return self
        while(runner.next!=None):
            runner=runner.next
        runner.next=new_node
        return self
    def remove_from_front(self):

        if(self.head!=None):
            self.head=self.head.next
            return self
        self.head=None
        return self
    def remove_from_back(self):
        runner=self.head

        if((self.head!=None)and(runner.next==None))or(self.head==None):
            self.remove_from_front
            return self
        else:
            while(runner.next.next!=None):
                runner=runner.next
            runner.next=None
            return self
    def remove_val(self, val):
        runner=self.head
        if(self.head.value==val)or(self.head==None):
            self.remove_from_front
            return self
        elif(runner.next!=None):
            while(runner.next.value!=val):
                 runner=runner.next
            runner.next=runner.next.next
            return self
        elif(runner.next==None):
            self.remove_from_back
            return self
    def insert_at(self, val, n):
        
        if(n==1):
            self.add_to_front
            return self
        elif(n>1):
            runner=self.head
            count=0
            while(runner!=None):
                count+=1
                if(count==n-1)and(runner.next!=None):
                    new_node=Node(val)
                    new_node.next=runner.next
                    runner.next=new_node
                    return self
                elif(count==n-1)and(runner.next==None):
                    self.add_to_back
                    return self
                runner=runner.next
            if(count<n):
                print(f'n should less or equal to {count}')
mylist=SList()
mylist.add_to_front('uyu').add_to_front(6).add_to_front(10).add_to_back(1).add_to_back(20)
mylist.remove_val(1).insert_at('iqiq',3).remove_from_front()
mylist.remove_from_front().remove_from_back().print_value().insert_at(20,4)
        
        