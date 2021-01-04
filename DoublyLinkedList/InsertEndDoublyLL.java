class Node{
    int data;
    Node next;
    Node prev;

    Node(int x){
        data=x;
        next=prev=null;
    }
}

class InsertEndDoublyLL{
    public static Node insertEnd(Node head,int key){
        Node r=new Node(key);
        if(head==null) return r;
        else{
            Node cur=head;
            while(cur.next!=null){
                cur=cur.next;
            }
            cur.next=r;
            r.prev=cur;
            return head;
        }
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
        head.next=t1;
        t1.next=t2;
        t2.next=null;
        t2.prev=t1;
        t1.prev=head;
        head=insertEnd(head,30);
        printList(head);
    }
}