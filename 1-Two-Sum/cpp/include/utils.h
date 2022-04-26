#ifndef UTILS_H
#define UTILS_H

#include <iostream>     // cout
#include <vector>       // vector
#include <algorithm>    // equal

namespace utils
{

    // Solution to the challenge
    class Solution {
        public:
            std::vector<int> twoSum(std::vector<int>& nums, int target) {
                std::vector<int> solution(2);

                return solution;
            }
    };

    // Test case function
    void testCase(const std::vector<int>& output_1, const std::vector<int>& output_2)
    {
        if (std::equal(output_1.begin(), output_1.end(), output_2.begin())) {
            std::cout << "Test passed" << "\n";
        } else {
            std::cout << "Test failed" << "\n";
        }
    }

} // namespace utils

#endif // UTILS_H
