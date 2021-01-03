class Node{
    int data;
    Node next;

    Node(int x){
        data=x;
        next=null;
    }
}

class InsertBeginCircularLL{
    public static Node insertBegin(Node head,int key){
        Node r=new Node(key);
        if(head==null) return r;
        else{
            Node cur=head;
            while(cur.next!=head){
                cur=cur.next;
            }
            cur.next=r;
            r.next=head;
            return r;
        }
       
    }
    public static void printList(Node head) {
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
        head.next.next.next=head;
        head=insertBegin(head,15);
        printList(head);
    }
}