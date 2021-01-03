class Node{
    int data;
    Node next;

    Node(int x){
        data=x;
        next=null;
    }
}

class SingleLL{
    static void print(Node head){
        while(head!=null){
            System.out.print(head.data+" ");
            head=head.next;
        }
    }
    public static void main(String[] args) {
        Node head=new Node(10);
        Node t1=new Node(20);
        Node t2=new Node(30);
        head.next=t1;
        t1.next=t2;
        print(head);
    }
}