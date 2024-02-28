#Q4. In an array, Count Pairs with given sum.

def count_pairs_with_sum(arr, target_sum):
    count = 0
    seen = set()
    
    for num in arr:
        complement = target_sum - num
        
        if complement in seen:
            count += 1
        
        seen.add(num)
    
    return count

arr = [1, 5, 7, -1, 5]
target_sum = 6
result = count_pairs_with_sum(arr, target_sum)
print("Number of pairs with sum", target_sum, ":", result)
