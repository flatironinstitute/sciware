#include <iostream>
#include <vector>
using std::cout; using std::endl;
using vec_type = std::vector<double>;

void print_vec(const vec_type &a) {
    for (const auto &el : a)
        cout << el << " ";
    cout << endl;
}

auto split_neg_pos(const vec_type &nums) {
    vec_type neg, pos;
    for (const auto &num : nums) {
        if (num < 0)
            neg.push_back(num);
        else
            pos.push_back(num);
    }
    return std::pair{neg, pos};
}

int main(int argc, char *argv[]) {
    vec_type nums;
    for (int i = -10; i < 10; ++i)
        nums.push_back(i);

    auto [neg, pos] = split_neg_pos(nums);
    print_vec(neg);
    print_vec(pos);

    return 0;
}
