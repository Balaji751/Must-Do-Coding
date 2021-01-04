class Node{
    int data;
    Node next;
    Node prev;

    Node(int x){
        data=x;
        next=prev=null;
    }
}

class DeleteTailDoublyLL{
    public static Node deleteTail(Node head){
        Node cur=head;
        while(cur.next.next!=null){
            cur=cur.next;
        }
        cur.next=null;
        return head;
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
        Node t1=new Node(20);
        Node t2=new Node(30);
        Node t3=new Node(40);
        head.next=t1;
        t1.next=t2;
        t2.next=t3;
        t3.next=null;
        t3.prev=t2;
        t2.prev=t1;
        t1.prev=head;
        head=deleteTail(head);
        printList(head);
    }
}