def sum_array(arr): return sum(arr)  
def avg_array(arr): return sum(arr) / len(arr)  
def find_index(arr, x): return arr.index(x) if x in arr else -1  
def contains(arr, x): return x in arr  
def remove_element(arr, x): return [i for i in arr if i != x]  
def copy_array(arr): return arr[:]  
def insert_at(arr, x, pos): return arr[:pos] + [x] + arr[pos:]  
def min_max(arr): return min(arr), max(arr)  
def reverse_array(arr): return arr[::-1]  
def find_duplicates(arr): return list({i for i in arr if arr.count(i) > 1})  
def common_values(arr1, arr2): return list(set(arr1) & set(arr2))  
def remove_duplicates(arr): return list(set(arr))  
def second_largest(arr): return sorted(set(arr))[-2] if len(set(arr)) > 1 else None  
def even_odd_count(arr): return sum(1 for i in arr if i % 2 == 0), sum(1 for i in arr if i % 2)  
def diff_largest_smallest(arr): return max(arr) - min(arr)  
def contains_12_23(arr): return 12 in arr and 23 in arr  
arr1, arr2 = [1, 2, 3, 4, 5, 2, 4, 6, 12, 23], [4, 5, 6, 7, 8]  
print(sum_array(arr1))  
print(avg_array(arr1))  
print(find_index(arr1, 3))  
print(contains(arr1, 5))  
print(remove_element(arr1, 4))  
print(copy_array(arr1))  
print(insert_at(arr1, 10, 2))  
print(min_max(arr1))  
print(reverse_array(arr1))  
print(find_duplicates(arr1))  
print(common_values(arr1, arr2))  
print(remove_duplicates(arr1))  
print(second_largest(arr1))  
print(even_odd_count(arr1))  
print(diff_largest_smallest(arr1))  
print(contains_12_23(arr1))