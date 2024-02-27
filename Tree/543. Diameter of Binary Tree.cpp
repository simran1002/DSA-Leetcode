'''
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
 This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
'''

class Solution {
    int height(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }
        int left = height(root->left);
        int right = height(root->right);
        int ans = max(left, right) + 1;
        return ans;
    }

public:
    int diameterOfBinaryTree(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }

        int left = diameterOfBinaryTree(root->left); 
        int right = diameterOfBinaryTree(root->right); 

        int opt1 = height(root->left) + height(root->right); 
        int opt2 = max(left, right); 

        return max(opt1, opt2);
    }
};


Time Complexity: O(n) (where n is the number of nodes in the binary tree)
Space complexity: O(h) (where h is the height of the binary tree)