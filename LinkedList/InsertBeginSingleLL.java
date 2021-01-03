class Node{
    int data;
    Node next;

    Node(int x){
        data=x;
        next=null;
    }
}

class InsertBeginSingleLL{
    public static Node insertBegin(Node head,int key){
        Node begin=new Node(key);
        begin.next=head;
        return begin;
    }
    public static void printList(Node head){
        Node cur=head;
        while(cur!=null){
            System.out.print(cur.data+" ");
            cur=cur.next;
        }
    }
    
    public static void main(String[] args) {
        Node head=new Node(20);
        head.next=new Node(30);
        head.next.next=new Node(40);
        // printList(head);
        head=insertBegin(head,10);
        printList(head);
    }
}