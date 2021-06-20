#problem :

# Write an Algorithm to output the minimum possible time to merge the given N subfiles into a single file
# Input: The input to the function/method consists of two arguments:
# numOfSubFiles: an integer representing the number of subfiles;
# files: a list of integers representing the size of the compressed subfiles
# Output: Return an integer representating the minimum time required to merge all the subfiles

# Constraints::
# 2 <= numOfSubFiles <= 10^6
# 1 <= files[i] <= 10^6

# Example:
# input:
# numOfSubFiles = 4
# files = [4,8,6,12]

# Output: 58

# Explanation:
# The optimal way to merge subfiles is as follows:
# Step 1: Merge the files of size 4 and 6 (time required is 10). Size of subfiles after merging. [8,10,12]
# Step 2: Merge the files of size 8 and 10 (time required is 18). Size of subfiles after merging. [18,12]
# Step 3: Merge the files of size 18 and 12 (time required is 30)
# Total time required to merge the file is 10 + 18 + 30 = 58.

# explanation https://www.lkouniv.ac.in/site/writereaddata/siteContent/202004032240235577anshu_singh_Optimal_merge_patterns.pdf

# ds : min heap

import heapq


def solution():
    size = int(input("total size :"))
    lst1 = [int(item) for item in input("Enter the list items : ").split()]

    heapq.heapify(lst1)
    one = heapq.heappop(lst1)
    two = heapq.heappop(lst1)

    total_time = one+two
    heapq.heappush(lst1,total_time)

    while len(lst1) > 1 :
        print('in while')
        subfile1 = heapq.heappop(lst1)
        subfile2 = heapq.heappop(lst1)
        heapq.heappush(lst1,subfile1+subfile2)

        total_time = total_time + subfile1 + subfile2

    return total_time

print(solution())


