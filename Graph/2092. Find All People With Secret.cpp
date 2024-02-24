'''
You are given an integer n indicating there are n people numbered from 0 to n - 1.
 You are also given a 0-indexed 2D integer array meetings where meetings[i] = [xi, yi, timei]
  indicates that person xi and person yi have a meeting at timei. A person may attend multiple meetings at the same time.
   Finally, you are given an integer firstPerson.
Person 0 has a secret and initially shares the secret with a person firstPerson at time 0. 
This secret is then shared every time a meeting takes place with a person that has the secret.
 More formally, for every meeting, if a person xi has the secret at timei, then they will share the secret with person yi,
  and vice versa.
The secrets are shared instantaneously. That is, a person may receive the secret and share it with people in other meetings
 within the same time frame.
Return a list of all the people that have the secret after all the meetings have taken place. You may return the answer in 
any order.
'''

class Solution {
public:
typedef pair<int, int> P;
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        map<int, vector<P>> timeMeetings;

        for(vector<int>& meeting: meetings) {
            int person1 = meeting[0];
            int person2 = meeting[1];
            int time = meeting[2];

            timeMeetings[time].push_back({person1, person2});
        }

        vector<bool> knowsSecret(n, false);
        knowsSecret[0] = true;
        knowsSecret[firstPerson] = true;
        
        for(auto&it : timeMeetings) {

            int t = it.first;
            vector<P> meets = it.second;


            unordered_map<int,vector<int>> adj;
            queue<int> que;
            unordered_set<int> alreadyAdded;

            for(auto& [person1, person2] : meets) {
                adj[person1].push_back(person2);
                adj[person2].push_back(person1);


                if(knowsSecret[person1] == true && alreadyAdded.find(person1) == alreadyAdded.end()) {
                    que.push(person1);
                    alreadyAdded.insert(person1);
                }

                if(knowsSecret[person2] == true && alreadyAdded.find(person2) == alreadyAdded.end()) {
                    que.push(person2);
                    alreadyAdded.insert(person2);
                }
            }

            while(!que.empty()) {
                int person = que.front();
                que.pop();

                for(auto &nextPerson : adj[person]) {
                    if(knowsSecret[nextPerson] == false) {
                        knowsSecret[nextPerson] = true;
                        que.push(nextPerson);
                    }
                }
            }
        }

        vector<int> result;
        for(int i=0; i<n; i++) {
            if(knowsSecret[i] == true) {
                result.push_back(i);
            }
        }

        return result;
            }
};

Time Complexity:
Space Complexity: