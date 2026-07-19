#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int longest_ones(vector<int> nums, int k) {
  int result = 0;
  int zero_counter = 0;
  int begin = 0;

  for (int end = 0; end < static_cast<int>(nums.size()); end++) {
    if (nums[end] == 0)
      zero_counter++;

    // shrinking condition, only executes when the window is invalid
    while (zero_counter > k) {
      if (nums[begin] == 0)
        zero_counter--;
      begin++;
    }
    result = max(result, end - begin + 1);
  }

  return result;
}

int main() {
  vector<int> nums = {1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0};
  int k = 2;

  cout << longest_ones(nums, k) << endl;
}
