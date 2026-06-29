# Problem - 844: backspace string compare


# time: o(n), space: O(1)
# class Solution:
def backspaceCompare(s: str, t: str) -> bool:
    p1 = len(s) - 1
    p2 = len(t) - 1

    while p1 >= 0 or p2 >= 0:
        # find valid character in s
        skip = 0
        while p1 >= 0:
            if s[p1] == "#":
                skip += 1
                p1 -= 1
            elif skip > 0:
                skip -= 1
                p1 -= 1
            else:
                break

        # find valid character in t
        skip = 0
        while p2 >= 0:
            if t[p2] == "#":
                skip += 1
                p2 -= 1
            elif skip > 0:
                skip -= 1
                p2 -= 1
            else:
                break

        # the index can be < 0 -> python evals it as reading from end
        if p1 >= 0 and p2 >= 0:
            if s[p1] != t[p2]:
                return False
        elif p1 >= 0 or p2 >= 0:
            # one has characters other doesnt
            return False

        # move forward for to not enter infinite-loop
        p1 -= 1
        p2 -= 1

    return True


# test

# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

s, t = "a", "aa#a"
# s, t = "a#c", "b"

print(backspaceCompare(s, t))
