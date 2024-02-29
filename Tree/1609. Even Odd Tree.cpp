'''
A binary tree is named Even-Odd if it meets the following conditions:
The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
'''

#include <queue>
#include <climits>  // Include for INT_MIN and INT_MAX

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isEvenOddTree(TreeNode* root) {
        if (!root) return true;  // Handle the case where the tree is empty

        std::queue<TreeNode*> que;
        que.push(root);

        bool even_level = true;

        while (!que.empty()) {
            int n = que.size();

            int prev;
            if (even_level)
                prev = INT_MIN;
            else
                prev = INT_MAX;

            while (n--) {
                TreeNode* curr = que.front();
                que.pop();

                if (even_level && (curr->val % 2 == 0 || curr->val <= prev)) {
                    return false;
                }

                if (!even_level && (curr->val % 2 != 0 || curr->val >= prev)) {
                    return false;
                }

                prev = curr->val;
                if (curr->left)
                    que.push(curr->left);

                if (curr->right)
                    que.push(curr->right);
            }

            even_level = !even_level;
        }

        return true;
    }
};


// Time complexity : O(n)
// Space Complexity : O(n)