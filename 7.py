#Q7. Move all the negative elements to one side of the array.

def move_negatives_to_one_side(arr):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        if arr[left] < 0 and arr[right] < 0:
            left += 1
        elif arr[left] >= 0 and arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] >= 0 and arr[right] >= 0:
            right -= 1
        else:
            left += 1
            right -= 1
    
    return arr
arr = [-1, 2, -3, 4, 5, -6, -7, 8, 9]
result = move_negatives_to_one_side(arr)
print(result)
