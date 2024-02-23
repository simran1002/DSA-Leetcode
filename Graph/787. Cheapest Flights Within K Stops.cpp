'''
There are n cities connected by some number of flights. You are given an array flights where
 flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops.
 If there is no such route, return -1.
 '''

 class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<vector<pair<int, int>>> graph(n);
        for (auto &flight : flights)
            graph[flight[0]].push_back({flight[1], flight[2]});
        
        vector<int> cost(n, (int)(1e9));
        queue<vector<int>> qu;
        qu.push({src, 0, 0});
        
        while (!qu.empty()) {
            auto flight = qu.front();
            qu.pop();

            int node = flight[0];
            int nodeCost = flight[1];
            int stops = flight[2];

            if (stops > k) continue;

            for (auto &[child, childCost] : graph[node]) {
                if (childCost + nodeCost < cost[child]) {
                    cost[child] = childCost + nodeCost;
                    qu.push({child, cost[child], stops + 1});
                }
            }
        }

        return cost[dst] == (int)(1e9) ? -1 : cost[dst];
    }
};

// Time Complexity: O(E * K), where E is the number of flights and K is the maximum number of stops allowed.
// Space Complexity: O(V + E), where V is the number of vertices (n in this case) and E is the number of flights.