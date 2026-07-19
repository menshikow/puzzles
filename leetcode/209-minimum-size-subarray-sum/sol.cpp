#include <algorithm>
#include <vector>

using namespace std;

// Input: target = 7, nums = [2,3,1,2,4,3]
// Output: 2

class Solution {
public:
  int minSubArrayLen(int target, vector<int> &nums) {
    int nsize();
    int left = 0;
    int sum = 0;
    int minLen = INT_MAX;

    for (int right = 0; right < n; right++) {
      sum += nums[right];

      while (sum >= target) {
        minLen = min(minLen, right - left + 1);
        sum -= nums[left];
        left++;
      }
    }

    return minLen == INT_MAX ? 0 : minLen;
  }
};
