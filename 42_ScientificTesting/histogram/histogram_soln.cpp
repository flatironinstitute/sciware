/*

CE LINK: https://godbolt.org/z/Yh94h7qo4

*/
#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

std::string read_text(const std::string &data_file) {
  std::ifstream ifs(data_file);
  std::stringstream stream;
  stream << ifs.rdbuf();
  return stream.str();
}

// note: more advanced version could avoid materializing this vector
// using e.g. generators (C++23)
std::vector<std::string_view> tokenize(std::string &text) {
  std::vector<std::string_view> result;
  size_t start = 0;
  while (start < text.size()) {
    size_t end = text.find_first_of(" \t\n", start);
    if (end == std::string::npos) {
      end = text.size();
    }
    auto token = std::string_view(text).substr(start, end - start);
    result.push_back(token);
    start = end + 1;
  }

  return result;
}

std::unordered_map<std::string_view, int>
count_tokens(std::vector<std::string_view> &tokens) {
  std::unordered_map<std::string_view, int> counts;
  for (const auto &t : tokens) {
    counts[t] += 1;
  }
  return counts;
}

void print_histogram(const std::unordered_map<std::string_view, int> &data,
                     int max_width, int total_data,
                     std::ostream &output = std::cout) {

  std::vector<std::pair<std::string, int>> sorted_data(data.begin(),
                                                       data.end());
  std::sort(sorted_data.begin(), sorted_data.end(),
            [](const auto &a, const auto &b) { return a.second > b.second; });

  for (size_t i = 0; i < 12 && i < sorted_data.size(); ++i) {
    auto &[token, n] = sorted_data[i];
    int width =
        std::min(static_cast<int>(std::floor(n * 9.0 / total_data)), max_width);
    std::string label = token + ":";
    output << std::left << std::setw(4) << label << std::string(width, '#')
           << std::endl;
  }
}

void histogram(const std::string &data_file, int max_width = 76) {
  auto text = read_text(data_file);
  auto tokens = tokenize(text);
  auto counts = count_tokens(tokens);

  print_histogram(counts, max_width, tokens.size());
}

#include <gtest/gtest.h>

TEST(histogram, tokenize) {
  std::string s{"foo bar baz bar foo"};
  auto tokens = tokenize(s);
  std::vector<std::string_view> expected{"foo", "bar", "baz", "bar", "foo"};
  EXPECT_EQ(tokens, expected);
}

TEST(histogram, tokenize_empty) {
  std::string s;
  auto tokens = tokenize(s);
  EXPECT_TRUE(tokens.empty());
}

TEST(histogram, counts) {
  std::vector<std::string_view> tokens{"foo", "bar", "baz", "bar", "foo"};
  auto counts = count_tokens(tokens);
  EXPECT_EQ(counts.size(), 3);
  EXPECT_EQ(counts["foo"], 2);
  EXPECT_EQ(counts["baz"], 1);
  EXPECT_EQ(counts["bar"], 2);
}

TEST(histogram, counts_empty) {
  std::vector<std::string_view> tokens{};
  auto counts = count_tokens(tokens);
  EXPECT_EQ(counts.size(), 0);
}

TEST(histogram, formatting) {
  std::unordered_map<std::string_view, int> counts;
  counts["AB"] = 300;
  counts["BC"] = 8000;
  counts["XY"] = 5492;
  counts["Z"] = 1200;
  std::string expected = "\
BC: ################################################################################\n\
XY: ################################################################################\n\
Z:  #########################################################\n\
AB: ##############\n";

  std::stringstream ss;
  print_histogram(counts, 80, 14992, ss);
  EXPECT_EQ(ss.str(), expected);
}

int main(int argc, char **argv) {
  // for illustration, we run an example before googletest
  // this is obviously not a test, so a 'finished' solution would remove it!
  histogram("histogram.data", 100);

  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
