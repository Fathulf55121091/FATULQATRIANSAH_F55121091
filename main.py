def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def print_array(arr):
    for element in arr:
        print(element, end=" ")
    print()

def main():
    print("Selamat datang di program pengurutan!")
    print("Pilih algoritma pengurutan yang ingin digunakan:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    choice = input("Masukkan pilihan (1/2): ")

    if choice == '1':
        # Bubble Sort
        arr = [64, 34, 25, 12, 22, 11, 90]
        print("Array sebelum pengurutan:")
        print_array(arr)
        bubble_sort(arr)
        print("Array setelah pengurutan menggunakan Bubble Sort:")
        print_array(arr)
    elif choice == '2':
        # Insertion Sort
        arr = [64, 34, 25, 12, 22, 11, 90]
        print("Array sebelum pengurutan:")
        print_array(arr)
        insertion_sort(arr)
        print("Array setelah pengurutan menggunakan Insertion Sort:")
        print_array(arr)
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

if _name_ == "_main_":
    main()