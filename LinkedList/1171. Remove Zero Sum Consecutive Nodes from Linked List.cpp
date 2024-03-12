'''
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum 
to 0 until there are no such sequences.
After doing so, return the head of the final linked list.  You may return any such answer.
'''

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeZeroSumSublists(ListNode* head) {
        int prefixSum = 0;
        unordered_map<int, ListNode*> mp;

        ListNode* dummyNode = new ListNode(0);

        dummyNode->next = head;

        mp[0] = dummyNode;

        while(head != NULL) {

            prefixSum +=head->val;

            if(mp.find(prefixSum) != mp.end()) {

                ListNode* Start = mp[prefixSum];
                ListNode* temp = Start;

                int pSum = prefixSum;

                while(temp != head) {

                    temp = temp->next;
                    pSum += temp->val;

                    if(temp != head)
                        mp.erase(pSum);
                }

                Start->next = head->next;

            } else {
                mp[prefixSum] = head;
            }

            head = head->next;
        }

        return dummyNode->next;
    }
};


Time Complexity: O(N)
Space Complexity: O(N)