data = [-1, 0, 3, 5, 9, 12]


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = left + (right - left) // 2
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1


print "Test " + str(search(data, -1))
print "Test " + str(search(data, 0))
print "Test " + str(search(data, 3))
print "Test " + str(search(data, 5))
print "Test " + str(search(data, 9))
print "Test " + str(search(data, 12))
print "Test " + str(search(data, 15))
