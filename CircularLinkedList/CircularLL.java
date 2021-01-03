class Node{
    int data;
    Node next;

    Node(int x){
        data=x;
        next=null;
    }
}


class CircularLL{
    public static void printList(Node head){
        System.out.print(head.data+" ");
        for(Node r=head.next;r!=head;r=r.next){
            System.out.print(r.data+" ");
        }
    }
    public static void main(String[] args) {
        Node head=new Node(10);
        head.next=new Node(20);
        head.next.next=new Node(30);
        head.next.next.next=head;
        printList(head);
    }
}