#include <iostream>
#include <vector>
using std::cout; using std::endl;
using vec_type = std::vector<int>;

void print_vec(const vec_type &a) {
    for (int i = 0; i < a.size(); ++i)
        cout << a[i] << " ";
    cout << endl;
}

void split_neg_pos(const vec_type &nums, vec_type &neg,
                   vec_type &pos) {
    neg.clear(); pos.clear();
    for (int i = 0; i < nums.size(); ++i) {
        if (nums[i] < 0)
            neg.push_back(nums[i]);
        else
            pos.push_back(nums[i]);
    }
}

int main(int argc, char *argv[]) {
    vec_type nums, neg, pos;
    for (int i = -10; i < 10; ++i) nums.push_back(i);

    split_neg_pos(nums, neg, pos);
    print_vec(neg);
    print_vec(pos);

    return 0;
}
