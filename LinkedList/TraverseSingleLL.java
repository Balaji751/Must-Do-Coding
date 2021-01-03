class Node{
    int data;
    Node next;
    Node(int x){
        data=x;
        next=null;
    }
}
class TraverseSingleLL{
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
        head.next.next=new Node(30);
        head.next.next.next=new Node(40);
        printList(head);
    }
}