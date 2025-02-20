# from typing import List


# def topKFrequent(nums: List[int], k: int) -> List[int]:
#     dict = {}

#     for i in nums:
#         if i not in dict:
#             dict[i] = 1
#         else:
#             dict[i] += 1
    
#     print(dict.items())
#     a = sorted(dict.items(), key=lambda x: x[1])  
#     a.reverse()  
#     print(a)

#     ls2 = []

#     for i in a[:k]:
#         ls2.append(i[0])
#     return ls2


# list1 = [1,1,1,2,2,3]
# print(topKFrequent(list1, 2))

# C++
# class Solution {
# public:
#     vector<int> topKFrequent(vector<int>& nums, int k) {
#         std::unordered_map<int, int> freqMap;
#         for (int num : nums) {
#             freqMap[num]++;
#         }

#         std::vector<std::pair<int, int>> freqVec(freqMap.begin(), freqMap.end());

#         std::sort(freqVec.begin(), freqVec.end(), [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
#             return a.second > b.second;
#         });

#         std::vector<int> result;
#         for (int i = 0; i < k; ++i) {
#             result.push_back(freqVec[i].first);
#         }

#         return result;
#     }
# };