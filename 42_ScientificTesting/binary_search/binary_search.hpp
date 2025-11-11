/*

CE LINK: https://godbolt.org/z/15E4MYaoz

TODO:
 - Test that the midpoint function works correctly.
 - Test that binary_search returns the correct index for a target in the list.
 - Test that binary_search returns -1 for a target not in the list.
*/

#pragma once
#include <vector>

inline int midpoint(int low, int high) { return (low + high) / 2; }

template <typename T> int binary_search(const std::vector<T> &data, T target) {
  int low = 0;
  int high = data.size() - 1;

  while (low <= high) {
    int mid = midpoint(low, high);
    auto &guess = data[mid];
    if (guess == target) {
      return mid;
    } else if (guess > target) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }
  return -1; // Item not found
}
