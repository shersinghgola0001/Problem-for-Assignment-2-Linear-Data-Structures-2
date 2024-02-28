#Q5. Find duplicates in an array.

def find_duplicates(arr):
    seen = set()
    duplicates = []

    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)

    return duplicates

arr = [4, 3, 2, 7, 8, 2, 6, 4, 8]
duplicate_elements = find_duplicates(arr)
print("Duplicate elements:", duplicate_elements)
