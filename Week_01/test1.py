class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        else:
            for j in nums2:
                for k in range(m):
                    if j < nums1[k]:
                        nums1.insert(k, j)
                        nums1.pop()
                        m = m + 1
                        break;
                    if j >= nums1[m - 1]:
                        nums1.insert(m, j)
                        nums1.pop()
                        m = m + 1
                        break;
