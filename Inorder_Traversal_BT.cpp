#include<bits/stdc++.h>
using namespace std;

class Node{
    
    public:
    int data;
    Node *left;
    Node *right;

};

Node* createnode(int data){
    Node *newnode = new Node();
    newnode->data = data;
    newnode->left = NULL;
    newnode->right = NULL;
    return newnode;
}


void inOrderTraveral(Node* node){
    if(node!=NULL){
        inOrderTraveral(node->left);
        cout<<node->data<<" ";
        inOrderTraveral(node->right);

    }
}

int main(){

    Node* p1 = createnode(1);
    Node* p2 = createnode(2);
    Node* p3 = createnode(3);
    Node* p4 = createnode(4);
    Node* p5 = createnode(5);
    Node* p6 = createnode(6);
    Node* p7 = createnode(7);
    Node* p8 = createnode(8);
    Node* p9 = createnode(9);
    Node* p10 = createnode(10);

    p1->left = p2;
    p2->left = p3;
    p3->left = p4;
    p4->right = p5;
    p2->right = p6;
    p5->left = p7;
    p1->right = p8;
    p8->right = p9;
    p9->left = p10;
    inOrderTraveral(p1);


    return 0;

}