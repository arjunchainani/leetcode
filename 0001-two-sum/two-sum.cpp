class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> valueToIndex;
        vector<int> result;

        for (int i = 0; i < nums.size(); ++i) {
            if (valueToIndex.find(target - nums.at(i)) != valueToIndex.end()) {
                result.push_back(i);
                result.push_back(valueToIndex[target - nums.at(i)]);
                return result;
            }
            valueToIndex[nums.at(i)] = i;
        }
        return result; 
    }
};