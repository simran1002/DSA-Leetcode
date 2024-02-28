'''
Given the root of a binary tree, return the leftmost value in the last row of the tree.
'''

class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        int leftmost_value;

        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();

            leftmost_value = node->val;

            if (node->right) {
                q.push(node->right);
            }
            if (node->left) {
                q.push(node->left);
            }
        }

        return leftmost_value;
    }
};


// Time complexity : O(N) ,where N is the number of nodes in the binary tree.
// Space complexity is O(W) ,where W is the maximum width (maximum number of nodes at any level) of the binary tree.