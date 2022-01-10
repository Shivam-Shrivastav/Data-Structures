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


void levelOrderTraveral(Node* node){
    if (node==NULL){
        return;
    }

    queue<Node*> q;
    q.push(node);
    q.push(NULL);
    while(!q.empty()){
        Node* node = q.front();
        q.pop();
        if(node != NULL){
            cout<<node->data<<" ";
            if(node->left)
                q.push(node->left);
            if(node->right)
                q.push(node->right);

        }
        else if(!q.empty()){
            q.push(NULL);
        }
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
    levelOrderTraveral(p1);


    return 0;

}