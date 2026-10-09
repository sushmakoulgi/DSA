from typing import Any


class DoubleLinkedNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None


class LRU:

    def __init__(self, capacity):
        self.capacity=capacity
        self.head=DoubleLinkedNode(0,0)
        self.tail=DoubleLinkedNode(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.cache={}

    def add_to_front(self,node:DoubleLinkedNode):
        hnext=self.head.next
        node.next=hnext
        hnext.prev=node
        self.head.next=node
        node.prev=self.head


    def remove(self,node):
        cnext=node.next
        cprev=node.prev

        cprev.next=cnext
        cnext.prev=cprev


    def put(self,key,value):
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self.remove(node=node)
            self.add_to_front(node=node)

        else:
            node=DoubleLinkedNode(key,value)
            if len(self.cache)< self.capacity:
                self.add_to_front(node)
                self.cache[key]=node
            else:
                lasnode=self.tail.prev
                self.remove(self.tail.prev)
                self.add_to_front(node)
                del self.cache[lasnode.key]
                self.cache[key]=node


    def print(self):
        itr=self.head.next
        l=[]
        while itr and itr.next is not None:
            l.append(f"{itr.key}+{itr.value}")
            itr=itr.next
        print(l)

    def get(self,key):
        if key in self.cache.keys():
            node=self.cache[key]
            self.remove(node)
            self.add_to_front(node)
            return node.value
        else:
            return -1

l=LRU(3)
l.get("A")
l.print()
l.put("A",1)
l.print()
l.put("B",2)
l.print()
l.put("C",3)
l.print()
l.put("D",4)
l.print()
