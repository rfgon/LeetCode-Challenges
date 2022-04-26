#include "../include/utils.h"

using namespace utils;

int main()
{
    // Test cases
    // Test 1
    std::vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    std::vector<int> output = {0, 1};

    // Test 2
    nums = {3, 2, 4};
    target = 6;
    output = {1, 2};

    // Test 3
    nums = {3, 3};
    target = 6;
    output = {0, 1};

    return 0;
}
