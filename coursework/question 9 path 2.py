class Node(object):
      def __init__(self, data):
          self.data=data
          self.next=None
          self.prev=None
 
class List(object):
      def __init__(self):
          self.head=None
          self.tail=None
      def insert(self, lis, node): # lis refers to head or tail.
          #Not actually perfect: how do we prepend to an existing list?
          if lis!=None: 
              node.next=lis.next 
              lis.next=node 
              node.prev=lis 
              if node.next!=None:
                  node.next.prev=node
          if self.head==None:
              self.head=self.tail=node
              node.prev=node.next=None
          elif self.tail==lis:
              self.tail=node
      def search(self,lis,num): # was gonna use it with clean but is now pointles
            x = num # search can still be used to find data in the double list
            if lis.data != x.data:  #also delete wont work without it if you use it without clean
                  y = lis.next
                  #print(y)
                  #print(x.data)
                  while y.data != x.data:
                              #print(y.data)
                              if y.data != x.data:
                                    y = y.next
                  #print(str(y) + "found it")
                  return(y)

      def delete(self,target):
            x = target
            #y = l.search(l.head,x) # functions i was gonna use with the search function
            #print(str(y) + "worked") #comment the bottem 2 out and replace with the 4 that are commented and you can use delete without clean
            #y.next.prev = y.prev
            #y.prev.next = y.next
            x.next.prev = x.prev
            x.prev.next = x.next

                        
      def clean(self, start):
            print("cleaning started")
            x = l.head
  
            y = x.next
        
            while y != None:
        
                  print(y.data)
                  if y.data == x.data:
                        l.delete(y)
                        y = y.next
                  else :
                        y = y.next
                        if y == l.tail:
                              if x.data == y.data:
                                    l.delete(x)
                                    x = x.next
                                    y = x.next
                              
                              print("loop")
                              x = x.next
                              y = x.next
                        elif x == l.tail :
                              break







            
      def display(self):
          data=[]
          n=self.head
          while n!=None:
              data.append(str(n.data))
              n=n.next
          print ("List: ",",".join(data))
         
if __name__ == '__main__':
      l=List()
      l.insert(None, Node(2))
      l.insert(l.head,Node(4))
      l.insert(l.head,Node(8))
      l.insert(l.head,Node(9))
      l.insert(l.head,Node(2))
      l.insert(l.head,Node(6))
      l.insert(l.tail,Node(8))
      #l.search(l.head,Node(8)) #example search
      #l.delete(Node(8))      #example delete
      l.clean(l.head)
      l.display()

print(l.tail)
