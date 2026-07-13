**1. I/O basics**
```cpp
#include <bits/stdc++.h>  // pulls in everything — very common in CP
using namespace std;

int n;
cin >> n;   // instead of scanf
cout << n;  // instead of printf
```
Add `ios_base::sync_with_stdio(false); cin.tie(0);` at the top of `main()` — makes cin/cout as fast as scanf/printf.

**2. `vector` — your new dynamic array**
```cpp
vector<int> a(n);        // array of size n
for (int i = 0; i < n; i++) cin >> a[i];
a.push_back(5);          // append
a.size();                // length
```
This alone replaces most manual `malloc`/array-size bookkeeping from C.

**3. `pair` and `tuple`** — bundle values together (e.g. value + original index)
```cpp
pair<int,int> p = {3, 5};
p.first; p.second;
```

**4. Sorting**
```cpp
sort(a.begin(), a.end());                    // ascending
sort(a.begin(), a.end(), greater<int>());    // descending
sort(a.begin(), a.end(), [](int x, int y){ return x > y; }); // custom (lambda)
```

**5. Key containers**
- `map<K,V>` / `unordered_map<K,V>` — like a hash table / dictionary
- `set<T>` / `unordered_set<T>` — unique sorted elements
- `queue`, `stack`, `priority_queue` (max-heap by default)

**6. Useful algorithms** (from `<algorithm>`)
```cpp
min(a,b), max(a,b), swap(a,b)
*max_element(a.begin(), a.end())
lower_bound(a.begin(), a.end(), x)  // binary search, needs sorted range
accumulate(a.begin(), a.end(), 0)   // sum of elements
```

**7. Range-based for loops + `auto`**
```cpp
for (auto x : a) cout << x << " ";       // read-only
for (auto &x : a) x *= 2;                // modify in place
```

**8. `string` class** — much friendlier than C strings
```cpp
string s;
cin >> s;
s.length(); s.substr(1,3); s + "abc"; s[i] // all just work
```

**9. `long long` for sums/products**.
