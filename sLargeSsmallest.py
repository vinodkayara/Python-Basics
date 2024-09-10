def getSecondLargest(nums):
    if len(nums) < 2:
        return -1
    largest, sLargest = float('-inf'), float('-inf')
    for num in nums:
        if num > largest:
            sLargest = largest 
            largest = num
        elif num > sLargest and num < largest:
            sLargest = num
    return sLargest

def getSecondSmallest(nums):
    if len(nums) < 2:
        return -1
    smallest, sSmallest = float('inf'), float('inf')
    for num in nums:
        if num < smallest:
            sSmallest = smallest
            smallest = num
        elif num < sSmallest and num != smallest:
            sSmallest = num
    return sSmallest

# Prompt the user for the number of elements
n = int(input("Enter number of elements: "))

# Prompt the user for the elements
nums = list(map(int, input(f"Enter {n} numbers: ").split()))

secondLargest = getSecondLargest(nums)
secondSmallest = getSecondSmallest(nums)

print("Second Largest: {}\nSecond Smallest: {}".format(secondLargest, secondSmallest))
