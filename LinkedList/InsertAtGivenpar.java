class Node{
    int data;
    Node next;
    Node(int x){
        data=x;
        next=null;
    }
}

class InsertAtGivenpar{
    public static Node insertAt(Node head,int pos,int key){
        Node at=new Node(key);
        int start=1;
        Node cur=head;
        while(cur!=null){
            if(start!=pos){
                start+=1;
                cur=cur.next;
            }
            at.next=cur.next;
            cur.next=at;
        }
        return cur;
        
    }
    public static void printList(Node head){
        Node cur=head;
        while(cur!=null){
            System.out.print(cur.data+" ");
            cur=cur.next;
        }
    }
    public static void main(String[] args) {
        Node head=new Node(10);
        head.next=new Node(20);
        head.next.next=new Node(40);
        insertAt(head,3,30);
        printList(head);
    }
}