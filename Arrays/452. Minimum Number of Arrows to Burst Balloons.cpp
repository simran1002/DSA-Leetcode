/*
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a
 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between 
 xstart and xend. You do not know the exact y-coordinates of the balloons.
Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon
 with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that 
 can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
*/

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        int n = points.size();

        sort(begin(points), end(points));

        vector<int> prev = points[0];

        int count = 1;

        for(int i = 1; i<n; i++) {
            int currStartPoint = points[i][0];
            int currEndPoint = points[i][1];

            int prevStartPoint = prev[0];
            int prevEndPoint = prev[1];

            if(currStartPoint > prevEndPoint) {
                count++;
                prev = points[i];
            } else {
                prev[0] = max(prevStartPoint, currStartPoint);
                prev[1] = min(currEndPoint, prevEndPoint);
            }
        }

        return count;
    }
};

// Time Complexity: O(nlogn)
// Space Complexity: O(1)