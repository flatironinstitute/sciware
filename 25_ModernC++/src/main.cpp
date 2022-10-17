#include <iostream>
#include <vector>

void split_neg_pos(const std::vector<int> &nums, std::vector<int> &neg, std::vector<int> &pos) {
    neg.clear();
    pos.clear();
    for (int i = 0; i < nums.size(); ++i) {
        if (nums[i] < 0)
            neg.push_back(nums[i]);
        else
            pos.push_back(nums[i]);
    }
}

int main(int argc, char *argv[]) {
    std::vector<int> nums;
    for (int i = 0; i < 20; ++i)
        nums.push_back(i - 10);

    std::vector<int> neg, pos;
    split_neg_pos(nums, neg, pos);

    for (int i = 0; i < neg.size(); ++i)
        std::cout << neg[i] << " ";
    std::cout << std::endl;

    for (int i = 0; i < pos.size(); ++i)
        std::cout << pos[i] << " ";
    std::cout << std::endl;

    return 0;
}
