class node:
    def __init__(self,data) -> None:
        self.data=data
        self.ref=None

class linkedlist:
    def __init__(self) -> None:
        self.head=None
    
    def add_begin(self,data):
        new_node=node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=node(data)
        new_node.ref=None
        n=self.head
        while n is not None:
            if n.ref is None:
                n.ref=new_node
                break
            n=n.ref

    def print_data(self):
        n=self.head
        while n is not None:
            print(n.data)
            n=n.ref

ll1=linkedlist()
ll1.add_begin(2)
ll1.add_begin(3)
ll1.add_end(7)
ll1.print_data()

        
