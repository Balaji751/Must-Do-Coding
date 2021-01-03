class Node{
    int data;
    Node next;
    Node(int x){
        data=x;
        next=null;
    }
}

class SearchSingleLL{
    public static int search(Node head,int key){
        if(head==null) return -1;
        int dis=1;
        while(head!=null){
            if(head.data==key) return dis;
            else{
                head=head.next;
                dis+=1;
            }
        }return -1;
    }
    public static void main(String[] args) {
        Node head=new Node(10);
        head.next=new Node(20);
        head.next.next=new Node(30);
        head.next.next.next=new Node(40);
        System.out.print(search(head,50));
    }
}