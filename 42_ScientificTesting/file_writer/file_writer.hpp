/*

CE LINK: https://godbolt.org/z/eheYq5T4r

TODO: Identify and test some of the properties of the DataProcessor class

 Suggestion:
  - Start with compute_value_2. Confirm that the 'draws' parameter
    actually controls the number of results

 Make sure that your tests leave your file system clean, and that tests
 run correctly regardless of the order in which they are called!

*/

#pragma once
#include <fstream>
#include <optional>
#include <ostream>
#include <random>
#include <string>
#include <vector>

#ifdef _WIN32
const char *PATH_SEPARATOR = "\\";
#else
const char *PATH_SEPARATOR = "/";
#endif

class FileInteractionManager {
public:
  FileInteractionManager(const std::string &root_dir = "output")
      : root_dir(root_dir) {}

  void save_1(double v) {
    std::string path = root_dir + PATH_SEPARATOR + "out1.txt";
    std::ofstream ofs(path);
    ofs << v << std::endl;
    ofs.close();
  }

  void save_2(std::vector<std::string> &v) {
    std::string path = root_dir + PATH_SEPARATOR + "out2.csv";
    if (v.empty()) {
      return;
    }
    std::ofstream ofs(path);
    ofs << *v.begin() << std::endl;
    for (auto s = v.begin() + 1; s != v.end(); ++s) {
      ofs << ',' << *s << std::endl;
    }
    ofs.close();
  }

  void save_3(int v) {
    std::string path = root_dir + PATH_SEPARATOR + "out3.txt";
    std::ofstream ofs(path);
    ofs << v << std::endl;
    ofs.close();
  }

private:
  std::string root_dir;
};

auto global_random = std::mt19937{std::random_device{}()};

class DataProcessor {
public:
  void compute_value_1() {
    std::uniform_real_distribution<double> dist(0.0, 1.0);
    result_1 = dist(global_random);
  }

  void compute_value_2(int draws = 3) {
    std::uniform_int_distribution<int> dist(0, options.size() - 1);
    auto res = std::vector<std::string>(draws);
    for (int i = 0; i < draws; ++i) {
      auto idx = dist(global_random);
      res[i] = options[idx];
    }
    result_2 = std::move(res);
  }

  void compute_value_3(int n = 3, double p = 0.5) {
    std::binomial_distribution<int> dist(n, p);
    result_3 = dist(global_random);
  }

  template <typename FIM> void write_files(FIM &file_mgr) {
    if (result_1) {
      file_mgr.save_1(*result_1);
    }
    if (result_2) {
      file_mgr.save_2(*result_2);
    }
    if (result_3) {
      file_mgr.save_3(*result_3);
    }
  }

private:
  std::vector<std::string> options = {"option 1", "option 2", "option 3",
                                      "option 4"};
  std::optional<double> result_1 = std::nullopt;
  std::optional<std::vector<std::string>> result_2 = std::nullopt;
  std::optional<int> result_3 = std::nullopt;
};
