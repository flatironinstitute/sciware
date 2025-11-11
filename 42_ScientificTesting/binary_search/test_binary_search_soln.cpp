#include <gtest/gtest.h>
#include <cmath>

#include "binary_search.hpp"

TEST(midpoint, massive) {
    auto mid = midpoint(std::pow(2, 31) - 4, std::pow(2, 31) - 2);
    EXPECT_EQ(mid, std::pow(2, 31) - 3);
}



















int main(int argc, char** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
