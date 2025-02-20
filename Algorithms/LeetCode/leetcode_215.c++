#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

class Solution {
  public:
      int findKthLargest(vector<int>& nums, int k) {
          
          std::priority_queue<int> pq(nums.begin(), nums.end());
  
          while(k - 1)
          {
              pq.pop();
              k--;
          }
          return pq.top();
  
  
      }
  };