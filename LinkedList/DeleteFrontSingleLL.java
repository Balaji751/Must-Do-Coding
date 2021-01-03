class Node{
    int data;
    Node next;
    Node(int x){
        data=x;
        next=null;
    }
}

class DeleteFrontSingleLL{
    public static Node deleteNode(Node head){
        if(head==null) return null;
        else{
            head=head.next;
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
        Node head=new Node(10);
        head.next=new Node(20);
        head.next.next=new Node(30);
        head.next.next.next=new Node(40);
        head=deleteNode(head);
        printList(head);
    }
}