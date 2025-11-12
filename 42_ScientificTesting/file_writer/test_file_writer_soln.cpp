/*

CE LINK: https://godbolt.org/z/8n8hPo9b3

*/

#include <gtest/gtest.h>

#include "file_writer.hpp"

struct MockFIM {
    double one;
    std::vector<std::string> two;
    int three;

    void save_1(double v){ one = v;}
    void save_2(std::vector<std::string>& v){ two = v; }
    void save_3(int v){ three = v; }
};

TEST(DataProcessor, Compute2DrawsSize) {
    DataProcessor dp{};
    dp.compute_value_2(7);

    // One solution: mock the file manager
    // Could also consider making the members accessible for testing
    // or reading the files from disk for the real version, plus cleanup
    MockFIM file_manager{};
    dp.write_files(file_manager);
    EXPECT_EQ(file_manager.two.size(), 7);
 }



















int main(int argc, char** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
