# 961. N-Repeated Element in Size 2N Array

**Problem type / Pattern:**
Array manipulation, set/hashmap usage, duplicate detection

**Difficulty:**
Easy

**Key idea / Algorithm:**

1. You are given an array of size `2N`.
2. Exactly one element is repeated N times; all others appear **once**.
3. **Naive approach:** Use a `Counter` or `map` to count occurrences → return the one with count > 1.
4. **Optimized approach (O(n) time, O(1) space):**

   * The repeated element must appear **at least twice consecutively or close**.
   * Check for duplicates among **nearby elements** (distance 1 or 2) while scanning the array.
5. **Set-based approach:** Keep a set of seen elements; return the first duplicate found.

**C++ Implementation (O(n) time, O(1) space, clever trick):**

```cpp
class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        int n = nums.size();
        for(int i = 0; i < n - 1; i++) {
            if(nums[i] == nums[i + 1] || (i < n - 2 && nums[i] == nums[i + 2]))
                return nums[i];
        }
        return nums[n-1]; // guaranteed to exist
    }
};
```

**Time / Space Complexity:**

* Set version: O(n) time, O(n) space
* Trick version: O(n) time, O(1) space

**Variants / Related Problems:**

* 217. Contains Duplicate → detect duplicates in an array
* 136. Single Number → work with unique and repeated elements
* 350. Intersection of Two Arrays II → count o
