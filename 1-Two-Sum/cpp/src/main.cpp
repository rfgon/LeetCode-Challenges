#include "../include/utils.h"

using namespace utils;

int main()
{
    Solution solution;

    // Test cases
    // Test 1
    std::vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    std::vector<int> output = {0, 1};

    testCase(output, solution.twoSum(nums, target));

    // Test 2
    nums = {3, 2, 4};
    target = 6;
    output = {1, 2};

    testCase(output, solution.twoSum(nums, target));

    // Test 3
    nums = {3, 3};
    target = 6;
    output = {0, 1};

    testCase(output, solution.twoSum(nums, target));

    return 0;
}
