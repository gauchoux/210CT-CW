class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None
 
class List(object):
      def __init__(self):
          self.head=None
          self.tail=None
      def insert(self,n,x):
          #Not actually perfect: how do we prepend to an existing list?
          if n!=None:
              x.next=n.next
              n.next=x
              x.prev=n
              if x.next!=None:
                  x.next.prev=x              
          if self.head==None:
              self.head=self.tail=x
              x.prev=x.next=None
          elif self.tail==n:
              self.tail=x
      def display(self):
          values=[]
          n=self.head
          while n!=None:
              values.append(str(n.value))
              n=n.next
          print ("List: ",",".join(values))



      def listrem(self, n):
            if n.prev != None:
                  n.prev.next = n.next
            else:
                  self.head = n.next
            if n.next != None:
                  n.next.prev = n.prev
            else:
                  self.tail = n.prev

      def deldup(self):                  #2,4,8,9,2,6,8
            nl = []
            a = self.head
            while a != None:
                  nl.append(a.value)
                  a = a.next
            nnl = []
            for i in nl:
                if i not in nnl:
                    nnl.append(i)
                    
            z = 0
            while z < len(nl):
                self.listrem(Node(nl[z]))
                z = z + 1
                
                        
            y = 1
            self.insert(None, Node(nnl[0]))
            while y < len(nnl):
                self.insert(self.head,Node(nnl[y]))
                y = y + 1
                
                            
                    
                  
                                          
         
if __name__ == '__main__':
      print("First List")
      l=List()
      l.insert(None, Node(2))
      l.insert(l.head,Node(4))
      l.insert(l.head,Node(8))
      l.insert(l.head,Node(9))
      l.insert(l.head,Node(2))
      l.insert(l.head,Node(6))
      l.insert(l.head,Node(8))
      l.display()

      print("============")
      print(" ")
      print("List without duplicates")
      l.deldup()
      l.display()
