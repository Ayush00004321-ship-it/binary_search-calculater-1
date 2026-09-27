# binary_search-calculater-1
def binary_search_with_steps(arr, target):
    low =0 
    high = len(arr) -1
    step = 0
    
    while low <= high:
        step += 1
        mid = (low + high) //2
        guess = arr[mid]
        
        print(f"step {step}: checking index {mid} (value: '{guess}')")
        if guess == target:
            return f"Found '{target}' at index {mid} in {step} steps."
        elif guess > target:
            high = mid -1
        else:
            low = mid + 1
            
    return f"'{target}' not found in list (toook {step} steps)."

name = [f"name_{i:03d}" for i in range(int(input( "your number:")))]

target_name = "name_005"
result = binary_search_with_steps(name, target_name)

print("\nResult:" ,result)
