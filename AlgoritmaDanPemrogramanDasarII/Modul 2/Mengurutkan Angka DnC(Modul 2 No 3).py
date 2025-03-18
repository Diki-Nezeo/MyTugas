def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2  # Membagi array menjadi dua bagian
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

if __name__ == "__main__":
    numbers = list(map(int, input("Masukkan angka yang akan diurutkan (pisahkan dengan spasi): ").split()))
    sorted_numbers = merge_sort(numbers)
    print("Hasil pengurutan:", sorted_numbers)
