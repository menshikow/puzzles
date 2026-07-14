#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void solve() {
    int n;
    cin >> n;
    string s;
    cin >> s;

    int max_streak = 0;
    int current_streak = 0;

    // Step 1: Find the longest continuous block of '#'
    for (int i = 0; i < n; i++) {
        if (s[i] == '#') {
            current_streak++;
            max_streak = max(max_streak, current_streak);
        } else {
            current_streak = 0; // Streak broken by '*'
        }
    }

    // Step 2: Calculate the time needed for the longest line
    if (max_streak == 0) {
        cout << 0 << "\n";
    } else if (max_streak == 1 || max_streak == 2) {
        cout << 1 << "\n";
    } else {
        // Since we erase 2 cm per second (1 from left, 1 from right):
        // A line of length L takes ceil(L / 2) seconds to erase.
        // In integer division, ceil(A / B) can be written as (A + B - 1) / B.
        cout << (max_streak + 1) / 2 << "\n";
    }
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}
