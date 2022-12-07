class a{
    node head;
    class node{
        int data;
        node next;
        node(int data){
            this.data=data;
            this.next=null;
        }
    }
    public void list(int data){
        node newnode = new node(data);
        if (head == null){
            head = newnode;
            return;
        }
        newnode.next = head;
        head=newnode;
    }
    public void addlast(int data){
        node newnode = new node(data);
        if (head == null){
            head = newnode;
            return;
        }
        node curr = head;
        while (curr.next != null){
            curr = curr.next;
        }
        curr.next = newnode;
    }
    
    public void print(){
        node curr = head;
        
        while(curr != null){
            System.out.print(curr.data + "-->");
            curr = curr.next;            
        }
        System.out.print("Null");
    }
    public void reverse(){
        
        if (head == null || head.next == null){
            return;
        }
        node previous = head; //null
        node current = head.next; //head
        
        while (current  != null){
            node temp = current.next;
            current.next = previous;
            previous = current;
            current = temp;
        }
        // head.next = null;                    
        head= previous;
    }
    
    public static void main(String[] args){
        a obj = new a();
        obj.list(10);
        obj.list(20);
        obj.addlast(20);
        obj.print();
    }
}

------------------------------------------------------------------------------------------------------------------

class a{
    node head = null;
    node tail = null;
    class node{
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
    }
    public static void main(String args[]){
        a obj =new a();
        obj.addlast(10);
        obj.addlast(20);
        obj.addlast(30);
        obj.addfirst(444);
        obj.addpos(99,4);
        obj.print();
    }
}