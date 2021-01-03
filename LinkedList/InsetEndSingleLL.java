class Node{
    int data;
    Node next;
    Node(int x){
        data=x;
        next=null;
    }
}

class InsetEndSingleLL{
    public static Node insertEnd(Node head,int x){
        Node end=new Node(x);
        if(head==null) return end;
        Node cur=head;
        while(cur.next!=null){
            cur=cur.next;
        }
       
        cur.next=end;
        return head;
    }
    public static void printList(Node head) {
        Node cur=head;
        while(cur!=null){
            System.out.print(cur.data+" ");
            cur=cur.next;
        }
    }
    public static void main(String[] args) {
        Node head=new Node(10);
        head.next=new Node(20);
        head.next.next=new Node(30);
        // printList(head);
        head=insertEnd(head,40);
        printList(head);
    }
}