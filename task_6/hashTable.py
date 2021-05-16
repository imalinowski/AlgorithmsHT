#!/usr/bin/env python
# coding: utf-8

# In[53]:


#Project

class Node:
    def __init__(self,key,val):
        self.value = val
        self.next = None
        self.prev = None
        self.key = key
        self.index = 0
        
class HashTable:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insertFirst(self,key,val):
        x = Node(key,val)
        if self.head == None and self.tail == None:
            self.head = x
            self.tail = x
            x.index = 0
        else:
            xy = self.head
            while xy:
                if xy.key == key:
                    xy.value = val
                    return
                xy = xy.next
            
            temp = self.head
            x.next = self.head
            x.index = 0
            self.head = x
            temp.prev = x
            self.__updateIndex(x.next,"insert")
            
    def insertLast(self,key,val):
        x = Node(key,val)
        if self.head == None and self.tail == None:
            self.head = x
            self.tail = x
        else:
            xy = self.head
            while xy:
                if xy.key == key:
                    xy.value = val
                    return
                xy = xy.next
                
            temp = self.tail
            temp.next = x
            self.tail = x
            self.tail.prev = temp
            x.index = temp.index + 1
            
    def insertAtIndex(self,index,key,val):
        xy = self.head
        while xy:
            if xy.key == key:
                xy.value = val
                return
            xy = xy.next
                
        if index == 0:
            self.insertFirst(key,val)
        elif index == self.length():
            self.insertLast(key,val)
        elif self.head != None and self.tail != None:
            x = Node(key,val)
            temp = self.head
            y = temp.next
            while y:
                if y.index == index:
                    x.prev = y.prev
                    y.prev.next = x
                    x.next = y
                    y.prev = x
                    x.index = index
                    self.__updateIndex(x.next,"insert")
                    break
                temp = temp.next
                y = y.next
            if not y:
                return "Index not reachable"
        else:
            return "Table is Empty"
            
    def __updateIndex(self,obj,case):
        if self.head == None and self.tail == None:
            return "Table is Empty"
        else:
            if case == "insert":
                x = obj
                while x:
                    x.index += 1
                    x = x.next
            elif case == "delete":
                x = obj
                while x:
                    x.index -= 1
                    x = x.next
                
    def getValueByIndex(self,index):
        if index > self.tail.index:
            return "index out of range"
        elif self.head == None and self.tail == None:
            return "Table is Empty"
        else:
            x = self.head
            while x:
                if x.index == index:
                    return x.value
                x = x.next
                
    def getValueByKey(self,key):
        if self.head == None and self.tail == None:
            return "Table is Empty"
        else:
            x = self.head
            while x:
                if x.key == key:
                    return x.value
                x = x.next
            return "key not found"
            
    def deleteFirst(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head != None and self.tail != None:
            self.head = self.head.next
            self.head.prev = None
            self.__updateIndex(self.head,"delete")
        else:
            return "Table is Empty"
        
    def deleteLast(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head != None and self.tail != None:
            temp = self.tail
            self.tail = temp.prev
            self.tail.next = None
        else:
            return "Table is Empty"
        
    def deleteByVal(self,val):
        if self.head == self.tail and self.head.value == val and self.tail.value == val:
            self.head = None
            self.tail = None
        elif self.head != None and self.tail != None:
            x = self.head
            if self.head.value == val:
                self.deleteFirst()
            elif self.tail.value == val:
                self.deleteLast()
            elif self.head == None and self.tail == None:
                return "Table is Empty"
            else:
                while x:
                    if x.value == val:
                        self.__updateIndex(x.next,"delete")
                        x.prev.next = x.next
                        x.next.prev = x.prev
                        break
                    x = x.next
                if not x:
                    return "Item Not found"
        else:
            return "Table is Empty"
        
    def deleteByIndex(self,val):
        if self.head == self.tail and self.head.index == val and self.tail.index == val:
            self.head = None
            self.tail = None
        elif self.head != None and self.tail != None:
            x = self.head
            if self.head.index == val:
                self.deleteFirst()
            elif self.tail.index == val:
                self.deleteLast()
            elif self.head == None and self.tail == None:
                return "Table is Empty"
            else:
                while x:
                    if x.index == val:
                        self.__updateIndex(x.next,"delete")
                        x.prev.next = x.next
                        x.next.prev = x.prev
                        break
                    x = x.next
                if not x:
                    return "Index Not found"
        else:
            return "Table is Empty"
        
    def deleteByKey(self,val):
        if self.head == self.tail and self.head.key == val and self.tail.key == val:
            self.head = None
            self.tail = None
        elif self.head != None and self.tail != None:
            x = self.head
            if self.head.key == val:
                self.deleteFirst()
            elif self.tail.key == val:
                self.deleteLast()
            elif self.head == None and self.tail == None:
                return "Table is Empty"
            else:
                while x:
                    if x.key == val:
                        self.__updateIndex(x.next,"delete")
                        x.prev.next = x.next
                        x.next.prev = x.prev
                        break
                    x = x.next
                if not x:
                    return "Key Not found"
        else:
            return "Table is Empty"

    def findByKey(self,key):
        if self.head == None and self.tail == None:
                return False
        x = self.head
        while x:
            if x.key == key:
                return True
            x = x.next
        return False
    
    def PrintkeyValues(self):
        if self.head == None and self.tail == None:
            return "Table is Empty"
        else:
            print("{",end="")
            x = self.head
            while x:
                print(str(x.key)+": "+str(x.value),end="")
                if x.next != None:
                    print(",",end=" ")
                x = x.next
        print("}")
        
    def printValues(self):
        if self.head == None and self.tail == None:
            return "Table is Empty"
        else:
            print("[",end="")
            x = self.head
            while x:
                print(x.value,end="")
                if x.next != None:
                    print(",",end=" ")
                x = x.next
        print("]")
        
    def printKeys(self):
        if self.head == None and self.tail == None:
            return "Table is Empty"
        else:
            print("[",end="")
            x = self.head
            while x:
                print(x.key,end="")
                if x.next != None:
                    print(",",end=" ")
                x = x.next
        print("]")
                
    def PrintReverse(self):
        if self.head == None and self.tail == None:
            return "Table is Empty"
        else:
            print("{",end="")
            x = self.tail
            while x:
                print(str(x.key)+": "+str(x.value),end="")
                if x.prev != None:
                    print(",",end=" ")
                x = x.prev
        print("}")
        
    def length(self):
        if self.head != None and self.tail != None:
            return self.tail.index + 1
        else:
            return "Table is Empty"
                
table = HashTable()

f_in =  open('input.txt')
f_out=  open('output.txt', 'w')

for line in f_in.readlines():
    print(line)
    if line[0]=='+':
        table.insertLast(line[1:],0)
    if line[0]=='-':
        table.deleteByKey(line[1:])
    elif line[0] == '?':
        f_out.write(str(table.findByKey(line[1:]))+'\n')
