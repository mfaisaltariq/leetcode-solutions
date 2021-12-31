from typing import List
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2

    if len(nums1) > len(nums2):
        A, B = B, A

    total_len = len(A) + len(B)
    half = total_len // 2
    left_pointer = 0
    right_pointer = len(A) -1


    while True:
        A_mid = (left_pointer + right_pointer) // 2
        B_mid = half - A_mid - 2 # minus 2 for index offset from total length as we need to minus 1 from both arrays
        print('pointer', left_pointer, right_pointer)
        print('mid', A_mid, B_mid, half)

        A_left = A[A_mid] if A_mid >= 0 else float("-infinity")
        A_right = A[A_mid +1] if A_mid+1 < len(A) else float("infinity")
        B_left = B[B_mid] if B_mid >= 0 else float("-infinity")
        B_right = B[B_mid + 1] if B_mid+1 < len(B) else float("infinity")
        print(A_left,A_right, 'here', B_left, B_right)

        if A_left <= B_right and B_left <= A_right:
            if total_len % 2 == 0:
                return (max(A_left, B_left) + min(B_right, A_right)) / 2

            return min(A_right, B_right)
        elif A_left > B_right:
            right_pointer = A_mid -1
        else:
            left_pointer = A_mid + 1


# print(findMedianSortedArrays([1,2,3,4,5,6,7,8], [1,2,3,4]))
print(findMedianSortedArrays([0, 0], [0, 0]))