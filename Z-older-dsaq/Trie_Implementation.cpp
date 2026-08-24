/*
    Your Trie object will be instantiated and called as such:
    Trie* obj = new Trie();
    obj->insert(word);
    bool check2 = obj->search(word);
    bool check3 = obj->startsWith(prefix);
 */
#include<bits/stdc++.h>
using namespace std;

struct Node {
    Node *links[26]; 
    bool flag = false; 
    
    bool containsKey(char ch) {
        return (links[ch - 'a'] != NULL); 
    }
    Node* get(char ch) {
        return links[ch-'a']; 
    }
    void put(char ch, Node* node) {
        links[ch-'a'] = node; 
    }
    void setEnd() {
        flag = true; 
    }
    bool isEnd() {
        return flag; 
    }
}; 
class Trie {
    private: Node *root; 
public:
    /** Initialize your data structure here. */
    Trie() {
        root = new Node(); 
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        Node *node = root;
        for(int i = 0;i<word.size();i++) {
            if(!node->containsKey(word[i])) {
                node->put(word[i], new Node()); 
            }
            node = node->get(word[i]); 
        }
        node->setEnd(); 
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        Node *node = root; 
        for(int i = 0;i<word.size();i++) {
            if(!node->containsKey(word[i])) {
                return false; 
            }
            node = node->get(word[i]); 
        }
        if(node->isEnd()) {
            return true; 
        }
        return false; 
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        Node *node = root; 
        for(int i = 0;i<prefix.size();i++) {
            if(!node->containsKey(prefix[i])) {
                return false; 
            }
            node = node->get(prefix[i]); 
        }
        return true; 
    }
};

int main(int argc, char const *argv[])
{
    Trie t1;
    string s = "apple";
    t1.insert(s);


    t1.insert("apps");
    t1.insert("apnx");
    t1.insert("bat");
    t1.insert("bac");
    t1.insert("battle");
    cout<<t1.search("battle");
    return 0;
}
