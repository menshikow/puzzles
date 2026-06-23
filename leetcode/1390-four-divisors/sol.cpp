#include <cmath>
#include <numeric>
#include <vector>

using namespace std;

class Solution {
public:
  int sumFourDivisors(vector<int> &nums) {
    int sum = 0;

    for (int num : nums) {
      vector<int> divisors;
      int limit = sqrt(num);

      for (int j = 1; j <= limit; j++) {
        if (num % j == 0) {
          divisors.push_back(j);
          if (j != num / j) {
            divisors.push_back(num / j);
          }
        }
      }

      if (divisors.size() == 4) {
        sum += accumulate(divisors.begin(), divisors.end(), 0);
      }
    }

    return sum;
  }
};
