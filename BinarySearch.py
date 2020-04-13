data = [-1, 0, 3, 5, 9, 12]


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    final_index = (len(nums) - 1) / 2
    left = False
    right = False
    while len(nums) >= 1:
        if left:
            if len(nums) % 2 == 0:
                index = len(nums) / 2
                final_index = final_index - index
            else:
                index = (len(nums) - 1) / 2
                final_index = final_index - 1 - index
            left = False
        elif right:
            if len(nums) % 2 == 0:
                index = len(nums) / 2
            else:
                index = (len(nums) - 1) / 2
            final_index = final_index + 1 + index
            right = False
        else:
            index = (len(nums) - 1) / 2
        if target == nums[index]:
            return final_index
        if target > nums[index]:
            nums = nums[(index + 1):]
            right = True
        elif target < nums[index]:
            nums = nums[:index]
            left = True
    return -1


print "Test " + str(search(data, -1))
print "Test " + str(search(data, 0))
print "Test " + str(search(data, 3))
print "Test " + str(search(data, 5))
print "Test " + str(search(data, 9))
print "Test " + str(search(data, 12))
print "Test " + str(search(data, 15))
