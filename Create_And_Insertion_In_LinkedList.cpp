#include<bits/stdc++.h>
using namespace std;

class Node{

	public:
	int data;
	Node *next;

};

void push(Node** head_ref, int data){

	Node* newnode = new Node();
	newnode->data = data;

	newnode->next = *head_ref;
	*head_ref = newnode;

}

void insertAfter(Node* prevNode, int data){
	if(prevNode->next==NULL){
		cout<<"The previous node cannot be null";
		return;
	}
	else{
		Node* newnode = new Node();
		newnode->data = data;
		newnode->next = prevNode->next;
		prevNode->next = newnode;

	}
}

void append(Node** head_ref, int data){

	Node* newnode = new Node();
	newnode->data = data;
	newnode->next = NULL;

	Node* last = *head_ref;

	if(*head_ref == NULL){
		*head_ref = newnode;
		return;
	}
	else{
		while(last->next!=NULL){
			last = last->next;
		}

	}
	
	last->next = newnode;
	return;

}

void printList(Node *node){
	while(node!=NULL){
		cout<<node->data<<" ";
		node = node->next;
	}

}

int main(){
	Node* head = NULL;
	append(&head, 6);
	push(&head, 5);
	push(&head, 7);
	push(&head, 4);
	push(&head, 2);
	insertAfter(head->next->next,1);
	push(&head, 9);
	printList(head);


	return 0;


}