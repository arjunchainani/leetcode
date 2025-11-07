class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string common_substr = "";

        for (int i = 0; i < strs[0].size(); ++i) {
            bool commonChar = true;
            for (int j = 0; j < strs.size() - 1; ++j) {
                if (i >= strs[j].size() || i >= strs[j + 1].size() || (strs[j].at(i) != strs[j + 1].at(i)))
                    return common_substr;
            }
            if (commonChar)
                common_substr.push_back(strs[0].at(i));   
        }
        return common_substr;
    }
};