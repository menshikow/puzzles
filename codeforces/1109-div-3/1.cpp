#include <algorithm>
#include <iostream>
#include <string>

void solve() {
  int n;
  std::cin >> n;
  std::string s;
  std::cin >> s;

  int max_streak = 0;
  int current_streak = 0;

  for (int i = 0; i < n; i++) {
    if (s[i] == '#') {
      current_streak++;
      max_streak = std::max(max_streak, current_streak);
    } else {
      current_streak = 0;
    }
  }

  if (max_streak == 0) {
    std::cout << 0 << "\n";
  } else if (max_streak == 1 || max_streak == 2) {
    std::cout << 1 << "\n";
  } else {
    std::cout << (max_streak + 1) / 2 << "\n";
  }
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(NULL);
  int t;
  std::cin >> t;

  while (t--) {
    solve();
  }
}
