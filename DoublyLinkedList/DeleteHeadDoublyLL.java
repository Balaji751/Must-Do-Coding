class Node{
    int data;
    Node next;
    Node prev;
    Node(int x){
        data=x;
        next=prev=null;
    }
}

class DeleteHeadDoublyLL{
    public static Node deleteHead(Node head){
        if(head==null) return null;
        if(head.next==null) return null;
        head=head.next;
        head.next.prev=null;
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
        Node head=new Node(5);
        Node t1=new Node(10);
        Node t2=new Node(20);
        Node t3=new Node(30);
        head.next=t1;
        t1.next=t2;
        t2.next=t3;
        t3.next=null;
        t3.prev=t2;
        t2.prev=t1;
        t1.prev=head;
        head=deleteHead(head);
        printList(head);
    }
}