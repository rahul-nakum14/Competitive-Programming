// https://www.programiz.com/java-programming/examples/linkedlist-implementation

class a{
    node head;
    node tail = null;
    static class node{
        int data;
        node next;
        
        node(int data){
            this.data = data;
            this.next=null;
        }
    }
    public void addfirst(int data){
        node newnode = new node(data);
        if (head == null){
            head = newnode;
            tail = newnode;
        }
        newnode.next =head;
        head = newnode;
    }
    public void addlast(int data){
        node newnode = new node(data);
        if (head == null){
            head=newnode;
            tail = newnode;
        }
        tail.next = newnode;
        tail = newnode;
    }
    
    public void addpos(int data,int pos){
        node newnode = new node(data);
        node curr = head;
        if (pos == 1){
            newnode.next = head;
            head = newnode;
            return;
        }
        
        else{
            for (int i = 1;i<pos-1;i++){
                curr  = curr.next;
            }
            newnode.next = curr.next;
            curr.next = newnode;
        }
    }
    
    public void print(){
        node curr = head;
        while (curr != null){
            System.out.print(curr.data + "-->");
            curr = curr.next;
        }
        System.out.println("Null");
    }
    public static void main(String args[]){
        a obj =new a();
        a.head = new node (10);
        node second = new node(20);
        node third = new node(30);
        
        a.head.next = second;
        second.next = third;

        // obj.addlast(10);
        // obj.addlast(20);
        // obj.addlast(30);
        // obj.addfirst(10);
        // obj.addfirst(20);
        // obj.addpos(99,4);
        
        obj.print();
    }
}