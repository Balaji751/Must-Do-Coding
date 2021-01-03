class Node{
    int data;
    Node next;
    Node(int x){
        data=x;
        next=null;
    }
}

class DeleteEndSingleLL{
    public static Node deleteEnd(Node head){
        if(head==null) return null;
        if(head.next==null) return null;
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
        System.out.println();
    }
    public static void main(String[] args) {
        Node head=new Node(10);
        head.next=new Node(20);
        head.next.next=new Node(30);
        head.next.next.next=new Node(40);
        printList(head);
        deleteEnd(head);
        printList(head);
    }
}