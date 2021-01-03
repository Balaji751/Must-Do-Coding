class Node{
    int data;
    Node next;
    Node(int x){
        data=x;
        next=null;
    }
}

class ToFindMiddleLL{
    public static int middleLL(Node head){
        int count=0;
        Node cur=head;
        while(cur!=null){
            count+=1;
            cur=cur.next;
        }
        Node temp=head;
        for(int i=0;i<count/2;i++){
            temp=temp.next;
        }
        return temp.data;
    }
    public static void main(String[] args) {
         Node head=new Node(10);
         head.next=new Node(20);
         head.next.next=new Node(30);
         head.next.next.next=new Node(40);
         head.next.next.next.next=new Node(50);
         System.out.print(middleLL(head));
    }
}
