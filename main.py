import time
import random
import matplotlib.pyplot as plt



def generate_randomarray(n):
    arr=[]
    for i in range(0,n,1):
        arr.append(random.randint(1,1000000))
    return arr



def insertion_sort(arr) :
    start = time.perf_counter()
    for i in range(1,len(arr)) :
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    end =time.perf_counter()
    print(        f"Running time for Insertion Sort with input size {len(arr)} "
                  f"is {round((end-start)*1000,5)} ms")
    return round((end-start)*1000,5)


def bubble_sort(arr):
    start=time.perf_counter()
    n=len(arr)
    for i in range(1,n):
        is_sorted =True
        for j in range(n-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                is_sorted = False
        if is_sorted:
            break
    end=time.perf_counter()
    print(  f"Running time for Bubble Sort with input size {len(arr)} "
            f"is {round((end-start)*1000,5)} ms")
    return round((end-start)*1000,5)



def selection_sort(arr):
    start=time.perf_counter()
    n = len(arr)
    for i in range (n-1):
        min_value = i
        for j in range(i+1,n):
            if arr[min_value]>arr[j]:
                min_value=j
        arr [i],arr[min_value]=arr[min_value],arr[i]
    end = time.perf_counter()
    print(        f"Running time for selection Sort with input size {len(arr)} "
                  f" is {round((end - start) * 1000, 5)} ms")
    return round((end - start) * 1000, 5)

def main():


    x=[1000,2000,5000,10000]

    arr1 = generate_randomarray(1000)
    arr2 = generate_randomarray(2000)
    arr3 = generate_randomarray(5000)
    arr4 = generate_randomarray(10000)


    y1i=insertion_sort(arr1.copy())
    y2i=insertion_sort(arr2.copy())
    y3i=insertion_sort(arr3.copy())
    y4i=insertion_sort(arr4.copy())
    yi= [y1i,y2i,y3i,y4i]


    y1s=selection_sort(arr1.copy())
    y2s=selection_sort(arr2.copy())
    y3s=selection_sort(arr3.copy())
    y4s=selection_sort(arr4.copy())
    ys=[y1s,y2s,y3s,y4s]


    y1b=bubble_sort(arr1.copy())
    y2b=bubble_sort(arr2.copy())
    y3b=bubble_sort(arr3.copy())
    y4b=bubble_sort(arr4.copy())
    yb=[y1b,y2b,y3b,y4b]

    # Quick sort
    # y1q = quick_sort(arr1.copy())
    # y2q = quick_sort(arr2.copy())
    # y3q = quick_sort(arr3.copy())
    # y4q = quick_sort(arr4.copy())
    # yq = [y1q, y2q, y3q, y4q]

    # Merge sort
    # y1m = merge_sort(arr1.copy())
    # y2m = merge_sort(arr2.copy())
    # y3m = merge_sort(arr3.copy())
    # y4m = merge_sort(arr4.copy())
    # ym = [y1m, y2m, y3m, y4m]

    # Heap sort
    # y1h = heap_sort(arr1.copy())
    # y2h = heap_sort(arr2.copy())
    # y3h = heap_sort(arr3.copy())
    # y4h = heap_sort(arr4.copy())
    # yh = [y1h, y2h, y3h, y4h]

    # Hybrid merge and selection sort
    # threshold = 6
    # y1hy = hybrid_merge_selection_sort(arr1.copy(), threshold)
    # y2hy = hybrid_merge_selection_sort(arr2.copy(), threshold)
    # y3hy = hybrid_merge_selection_sort(arr3.copy(), threshold)
    # y4hy = hybrid_merge_selection_sort(arr4.copy(), threshold)
    # yhy = [y1hy, y2hy, y3hy, y4hy]


    plt.plot(x, yi, label='insertion sort', color='green', linestyle='-', marker='o')
    plt.plot(x, ys, label='selection sort', color='red', linestyle='-', marker='o')
    plt.plot(x, yb, label='bubble sort', color='blue', linestyle='-', marker='o')
    # plt.plot(x, yq, label='quick sort', color='purple', linestyle='-', marker='o')
    # plt.plot(x, ym, label='merge sort', color='orange', linestyle='-', marker='o')
    # plt.plot(x, yh, label='heap sort', color='brown', linestyle='-', marker='o')
    # plt.plot(x, yhy, label='hybrid merge-selection sort', color='black', linestyle='-', marker='o')



    plt.grid(True)

    plt.xlabel('input size (N)')
    plt.ylabel('Execution time(ms)')
    plt.title('(example graph)')

    plt.legend()
    plt.show()




if __name__ == "__main__":
    main()