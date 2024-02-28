#Q6. Find the Kth largest and Kth smallest number in an array.

def kth_largest_and_smallest(arr, k):
    arr.sort()
    kth_smallest = arr[k - 1]
    kth_largest = arr[-k]
    return kth_smallest, kth_largest

arr = [3, 1, 7, 2, 8, 4]
k = 3
kth_smallest, kth_largest = kth_largest_and_smallest(arr, k)
print(f"{k}th smallest: {kth_smallest}")
print(f"{k}th largest: {kth_largest}")
