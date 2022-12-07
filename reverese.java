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
    public void addlast(int data){
        node newnode = new node(data);
        if (head == null){
            head=newnode;
            tail = newnode;
        }
        tail.next = newnode;
        tail = newnode;
    }
    public void reverse(){
        node curr = head;
        while (curr.next != tail){
            System.out.print(tail.data + "-->");
            curr = curr.next;
        }
        tail.next = curr.next;
    }
    public void delfirst(){
        if (head==null){
            System.out.println("Empty");
            return;
        }
        head = head.next;
    }
    public void dellast(){
        if (head.next == null){
            return;
        }
        node secondlast = head;
        node last= head.next;
        
        while (last.next != null){
            secondlast = secondlast.next;
            last = last.next;
        }
        secondlast.next = null;
        return;
    }
    public void delpos(int pos){
        
        node previous = head;
        node current = head.next;
        
        if (pos == 1){
            head= head.next;
            return;
        }
        
        for (int i = 1 ; i<pos-1;i++){
            previous = previous.next;
            current = current.next;
        }
        previous.next = current.next;
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
        obj.print();
        obj.reverse();
    }
}