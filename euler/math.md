# Projet euler problem solving 

- doing more with less code

## Mathematical Topics to research on

### **1. Modular Arithmetic (The "Clock" Math)**
Project Euler often asks for the last 10 digits of a massive number or involves cycles.
*   **Concepts:** Congruences, Modular Exponentiation, and the **Chinese Remainder Theorem**.
*   **Why:** This allows you to perform calculations on numbers with millions of digits without actually storing the whole number in memory—essential for keeping your C++ code "nano" and fast.

### **2. Prime Theory & Sieving**
Primes are the "atoms" of Project Euler.
*   **Concepts:** **Sieve of Eratosthenes** (and the segmented version), Primality testing (Miller-Rabin), and Prime Factorization.
*   **Why:** Many problems require checking millions of numbers for primality. A basic `is_prime` function won't cut it; you’ll need to implement high-performance sieves in C++.

### **3. Combinatorics & Generating Functions**
This helps you count possibilities without actually iterating through them.
*   **Concepts:** Binomial Coefficients ($nCr$), Pascal’s Triangle, and **Inclusion-Exclusion Principle**.
*   **Why:** Problems involving "How many paths through a grid" or "How many ways to make change" are solved instantly with these formulas, whereas a recursive search might take years to finish.

### **4. Diophantine Equations**
These are polynomial equations where you only care about integer solutions.
*   **Concepts:** **Linear Diophantine Equations** and **Pell’s Equation**.
*   **Why:** Many mid-to-high-level Euler problems boil down to finding integer solutions to equations like $x^2 - Dy^2 = 1$. Knowing the algorithm for continued fractions will save you days of frustration.

### **5. Computational Geometry**
Since you’ve worked on the **orrery** gravity simulator, you’ll find these problems intuitive.
*   **Concepts:** Pick's Theorem, Shoelace Formula (for area), and Integer-only Coordinate Geometry.
*   **Why:** Some problems ask about points inside triangles or circles on a grid. Using integer-only math avoids the floating-point errors you might encounter in your numerical libraries.

**Pro-Tip for C++:** 
Since you are a minimalist, you’ll likely enjoy writing your own `BigInt` class for Euler problems that exceed the `uint64_t` limit. It’s a classic C++ rite of passage!



### **1. The Inclusion-Exclusion Principle (Combinatorics)**
Many Euler problems ask you to count items that satisfy at least one of several properties. 
*   **The Concept:** To find the size of the union of multiple sets, you sum the sizes of the individual sets, subtract the sizes of all two-set intersections, add the sizes of all three-set intersections, and so on.
*   **Euler Application:** Problems like "How many numbers below $10^{18}$ are divisible by 3, 5, or 7?"
*   **C++ Tip:** This is often implemented using **Bitmasks**. You can iterate from $i = 1$ to $2^n - 1$ to represent every possible combination of properties.



### **2. Continued Fractions**
This is a niche area of math that is surprisingly dominant in Project Euler.
*   **The Concept:** Representing a number (especially square roots) as an iterative fraction: $a_0 + \frac{1}{a_1 + \frac{1}{a_2 + \dots}}$.
*   **Euler Application:** This is the standard way to solve **Pell’s Equation** ($x^2 - Dy^2 = 1$), which appears in many problems involving large integer solutions to quadratic equations.
*   **Why it's cool:** It allows you to find the best possible rational approximations ($p/q$) for irrational numbers.

### **3. Dynamic Programming (DP) on Digits**
Since you are a programmer, you likely know DP, but "Digit DP" is a specific sub-type for math problems.
*   **The Concept:** Instead of iterating through numbers from $1$ to $10^{15}$ (which would take years), you build the number digit-by-digit while keeping track of a state (e.g., the current sum of digits, or whether the number is still below the limit).
*   **Euler Application:** Problems that ask: "How many numbers below $10^{15}$ have the property that the sum of their digits is prime?"
*   **C++ Tip:** Use a memoization table `memo[digit_pos][current_sum][is_less]` to store results and avoid redundant calculations.



### **4. Fast Powering & Matrix Exponentiation**
You have a library called **numerica**; this topic belongs there.
*   **The Concept:** You can calculate $a^n \pmod m$ in $O(\log n)$ time using **Binary Exponentiation**. More impressively, you can find the $n$-th Fibonacci number in $O(\log n)$ time using **Matrix Exponentiation**.
*   **Euler Application:** When a problem asks for the $10^{18}$-th term of a sequence defined by a linear recurrence.
*   **Why it's essential:** At $n = 10^{18}$, even a simple `for` loop will take decades to finish. Binary exponentiation finishes in about 60 operations.

### **The "Eulerian" Workflow for a C++ Dev**
1.  **Paper First:** Spend 30 minutes with a pen and paper. If you start coding immediately, you’ve probably already lost.
2.  **Look for Symmetry:** Can you solve half the problem and multiply by two? 
3.  **The Small Case:** Write a brute-force version for $N=10$ or $N=100$. Look at the output. Does it match a known sequence (like the Mersenne primes or Triangular numbers)?
4.  **Use `__int128_t`:** Since you use GCC/Clang for your C++ projects, remember that `__int128_t` exists. It’s a lifesaver for intermediate calculations that exceed `uint64_t` but don't quite need a full `BigInt` library.

Which of these sounds like it would have helped you on a problem you've seen recently?
