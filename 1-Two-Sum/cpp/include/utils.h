#ifndef UTILS_H
#define UTILS_H

#include <iostream>     // cout
#include <vector>       // vector
#include <algorithm>    // equal

namespace utils
{

    // Solution to the challenge
    class Solution
    {
        public:
            std::vector<int> twoSum(std::vector<int>& nums, int target)
            {
                std::vector<int> solution(2);

                bool found_indices = false;

                // Try every combination of numbers pairs
                for (int i = 0; i < (int)nums.size(); ++i) {
                    for (int j = i + 1; j < (int)nums.size(); ++j) {
                        if (nums.at(i) + nums.at(j) == target) {
                            solution.at(0) = i;
                            solution.at(1) = j;
                            found_indices = true;
                            break;
                        }
                    }

                    if (found_indices) {
                        break;
                    }
                }

                return solution;
            }
    };

    // Test case
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
