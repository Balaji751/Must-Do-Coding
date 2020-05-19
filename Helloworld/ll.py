class Node:
	def __init__(self,data):
		self.data=data
		self.next=None


class LL:
	def __int__(self):
		self.head=None


	def printList(self):
		temp=self.head
		while(temp):
			print (temp.data)
			temp=temp.next

	def add(self,new_data):
		new_node=Node(new_data)
		new_node.next=self.head
		self.head=new_node

	def append(self,new_data):
		new_node=Node(new_data)
		if self.head is None:
			self.head=new_node
			return

		last=self.head
		while(last.next):
			last=last.next

		last.next=new_node

if __name__ =='__main__':
	llist=LL()
	llist.head=Node(1)
	second=Node(2)
	third=Node(3)

	llist.head.next=second
	second.next=third
	
	llist.add(4)
	llist.append(9)
	llist.printList()