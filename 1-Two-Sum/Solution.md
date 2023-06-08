---
created: "2023-06-08 18:17:59"
tags: [" #leetcode "]
aliases: [""]
---
# Solution

```
Input: Array of integers
Output: Indices of input array

loop through array starting at index n:
	loop through array starting at index m = n+1:
		sum = array[n] + array[m]
		if sum equals target value:
			return indices n and m
```
