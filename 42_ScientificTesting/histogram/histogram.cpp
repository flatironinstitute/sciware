/*

CE LINK: https://godbolt.org/z/r469v4z3W

TODO: Write a set of narrowly focused tests for the code in this file.
 Be sure to cover all its important properties.
 You can make whatever changes you want to the code, but be sure
 not the change the user-facing interface of the histogram function.

   Hint:
 When you're thinking about the important properties of the function,
 think about whether its operations have a natural grouping.
 How can you make it easier to test those individually?
*/

#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

inline void histogram(const std::string &data_file, int max_width = 76) {
  std::unordered_map<std::string, int> data;
  int total_data = 0;
  std::ifstream ifs(data_file);
  std::string line;
  while (std::getline(ifs, line)) {
    size_t start = 0;
    while (start < line.size()) {
      size_t end = line.find_first_of(" \t", start);
      if (end == std::string::npos) {
        end = line.size();
      }
      auto token = line.substr(start, end - start);
      data[token] += 1;
      total_data += 1;
      start = end + 1;
    }
  }
  ifs.close();

  std::vector<std::pair<std::string, int>> sorted_data(data.begin(),
                                                       data.end());
  std::sort(sorted_data.begin(), sorted_data.end(),
            [](const auto &a, const auto &b) { return a.second > b.second; });

  for (size_t i = 0; i < 12 && i < sorted_data.size(); ++i) {
    auto &e = sorted_data[i];
    int n = e.second;
    int width =
        std::min(static_cast<int>(std::floor(max_width * n * 9.0 / total_data)),
                 max_width);
    std::string label = e.first + ":";
    std::cout << std::left << std::setw(4) << label << std::string(width, '#')
              << std::endl;
  }
}

int main() { histogram("histogram.data", 100); }
