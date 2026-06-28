# notes on the problem 

- REWRITE IN NUMPY


- the idea is to find the max sums of each line, each row and each diagonal



Here's a reading list mapped to the gaps in your solution, with the concept and why it matters:

**1. Direction vectors / delta encoding**
Look up how grid-traversal problems (common in Project Euler, and in graph problems like flood fill or Dijkstra on grids) represent "the 8 directions a cell can go" as a set of `(dx, dy)` pairs — e.g., right is `(0, 1)`, down-left is `(1, -1)`. This is the standard fix for your diagonal problem: instead of writing separate logic for "diagonal" and "anti-diagonal," you iterate over a small list of direction pairs and reuse the same stepping logic for all 8. Search: "grid traversal direction vectors" or look at how flood-fill algorithms enumerate neighbors.

**2. Brute force vs. optimization — when complexity is justified**
Read about **time complexity classes** (the formal version of "how does runtime grow as input grows," usually written as O(n), O(n²), etc.) specifically the idea that constant factors (like your window size of 4) don't change the complexity class, so optimizing them is usually wasted effort. A good framing to search: "premature optimization" alongside Big-O notation — this explains *why* your sliding window added cost without lowering complexity class.

**3. Sliding window — and where it actually breaks**
Now that you've seen it fail on products, read specifically about **what operations sliding window techniques require** (an invertible, associative combining operation — sum and addition/subtraction is the classic case). Then read about **why products don't get the same treatment** — this is usually discussed alongside "maximum product subarray" problems (a well-known variant of the classic "maximum sum subarray" / Kadane's algorithm). Reading why the product version needs *extra* state (tracking both max and min running product, because multiplying by a negative flips them) will sharpen your intuition for when a technique generalizes and when it doesn't.

**4. Boundary checking / off-by-one errors**
This is worth treating as its own topic, not just an Euler detail. Read about **off-by-one errors** generally — they're the single most common source of "code runs, gives a plausible-looking wrong answer" bugs, which is exactly the failure mode you're at risk of with diagonals. The mental model worth internalizing: before indexing, always ask "what's the last valid starting position such that stepping N times stays in bounds," rather than checking inside the loop.

**5. Prefix sums (optional, but a good adjacent concept)**
Not required for this problem, but since you're thinking about "avoid recomputation," prefix sums are the *correct* place to apply that instinct — they let you get the sum of any contiguous range in constant time after one preprocessing pass. Reading this will help you recognize, in the future, situations where window-style incremental computation is actually warranted (range sums, range queries) versus where it's not (fixed tiny windows like this one).

If you want a single most-useful thing to actually read code for: search "Project Euler 11 solutions discussion" on places like the Project Euler forums — seeing how others handle the 8-direction enumeration cleanly will make the direction-vector idea concrete rather than abstract.

