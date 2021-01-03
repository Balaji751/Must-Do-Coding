class Node{
    int data;
    Node next;

    Node(int x){
        data=x;
        next=null;
    }
}

class DeleteHeadCircularLL{
    public static Node deleteHead(Node head){
        if(head==null) return null;
        if(head.next==null) return null;
        else{
            Node cur=head;
            while(cur.next!=head){
                cur=cur.next;
            }
            cur.next=head.next;
            return cur.next;
        }
    }
    public static void printList(Node head){
        System.out.print(head.data+" ");
        Node r=head.next;
        while(r!=head){
            System.out.print(r.data+" ");
            r=r.next;
        }
    }
    public static void main(String[] args) {
        Node head=new Node(10);
        head.next=new Node(20);
        head.next.next=new Node(30);
        head.next.next.next=new Node(40);
        head.next.next.next.next=head;
        head=deleteHead(head);
        printList(head);
    }
}