// 十大经典排序算法代码

#1冒泡排序

# def bubble_sort(arr):
#     for i in range(len(arr)-1):
#         for j in range(0,len(arr)-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#
#     return arr


#2快速排序

# def quick_sort(arr,first,last):
#     if first>=last:
#         return arr
#     pivot,low,high=arr[first],first,last
#     while low<high:
#         while low<high and arr[high]>=pivot:
#             high-=1
#         arr[low]=arr[high]
#
#         while low<high and arr[low]<pivot:
#             low+=1
#         arr[high]=arr[low]
#     arr[low]=pivot
#
#     quick_sort(arr,first,low-1)
#     quick_sort(arr,low+1,last)
#
#     return arr


#3选择排序

# def selection_sort(arr):
#     for i in range(len(arr)-1):
#         min=i
#         for j in range(i+1,len(arr)):
#             if arr[j] < arr[min]:
#                 min=j
#         if i != min:
#             arr[i],arr[min]=arr[min],arr[i]
#
#     return arr


#4堆排序

# #4_1堆化
# #当前i节点及largest节点的向下节点
# def heapify(arr,length,i):
#     largest=i
#     left=2*i+1
#     right=2*i+2
#     if left<length and arr[left]>arr[largest]:
#         largest=left
#     if right<length and arr[right]>arr[largest]:
#         largest=right
#     if largest!=i:
#         arr[i],arr[largest]=arr[largest],arr[i]
#         heapify(arr,length,largest)
#
# #4_2堆排序
# def heap_sort(arr):
#     length=len(arr)
#     #建立最大堆(从下往上走)
#     for i in range(length,-1,-1):
#         heapify(arr,length,i)
#     #去掉最大值并更新堆
#     for i in range(length-1,0,-1):
#         arr[0],arr[i]=arr[i],arr[0]
#         heapify(arr,i,0)
#
#     return arr


#5插入排序

# def insert_sort(arr):
#     for i in range(1,len(arr)):
#         cur=arr[i]
#         j=i
#         while j>0 and arr[j-1]>cur:
#             arr[j]=arr[j-1]
#             j-=1
#         arr[j]=cur
#
#     return arr


#6希尔排序

# def shell_sort(arr):
#     gap=len(arr)//2
#     while gap>0:
#         #处理该gap下的插入排序
#         for i in range(gap,len(arr)):
#             cur=arr[i]
#             j=i
#             while j-gap>=0 and arr[j-gap]>cur:
#                 arr[j]=arr[j-gap]
#                 j-=gap
#             arr[j]=cur
#         #缩短步长
#         gap=gap//2
#
#     return arr


#7归并排序

# #7_1数组合并
# def merge(left,right):
#     result=[]
#     while left and right:
#         if left[0]<right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     if left:
#         result+=left
#     if right:
#         result+=right
#
#     return result
#
# #7_2归并排序
# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
#     mid=len(arr)//2
#     left=arr[:mid]
#     right=arr[mid:]
#     left=merge_sort(left)
#     right=merge_sort(right)
#
#     return merge(left,right)


#8计数排序
"""
1.生成(1~max)的数组count，统计count中每个数在arr中的数目
2.统计arr中每个数比它小的数目，也就是每个count的值和前一个数的值相加
3.输出数组out，小于它的数就是out数组的下标
"""
# def count_sort(arr):
#     length=len(arr)
#     max_value=max(arr)
#     count=[0 for _ in range(max_value+1)]
#     output=[0 for _ in range(length)]
#     # count=[0]*(max_value+1)
#     # output=[0]*(length)
#
#     #统计每个数的数目
#     for i in range(length):
#         count[arr[i]]+=1
#     print(count)
#     #统计小于等于arr[i]的数的个数，假设为m
#     for i in range(1,len(count)):
#         count[i]+=count[i-1]
#     print(count)
#     for i in range(length):
#         #m为小于等于arr[i]的数目，则小于m的数为m-1个，下标从零开始，所以标记为m-1即count[arr[i]]-1
#         output[count[arr[i]]-1]=arr[i]
#         #针对重复数字，所以反向填充目标数组，将每个数字的统计减去 1
#         count[arr[i]]-=1
#
#     return output


#9桶排序
# def bucket_sort(arr):
#     buckt=[0]*(max(arr)+1)
#     result=[]
#     for i in arr:
#         buckt[i]+=1
#     for num in range(len(buckt)):
#         if buckt[num]!=0:
#             for j in range(buckt[num]):
#                 result.append(num)
#
#     return result


#10基数排序

def radix_sort(arr):
    i=0
    j=len(str(max(arr)))
    while i < j:
        bucket_list=[[] for i in range(10)]
        for x in arr:
            bucket_list[int(x/(10**i))%10].append(x)
        arr.clear()
        for x in bucket_list:
            for y in x:
                arr.append(y)

        i+=1

    return arr


if __name__ == '__main__':
    list=[1,5,3,3,12,20,7,9,30,4]
    print('排序前：',list)
    #冒泡排序
    # result=bubbleSort(list)

    #快速排序
    # result = quick_sort(list,0,len(list)-1)

    #选择排序
    # result=selection_sort(list)

    #堆排序
    # result=heap_sort(list)

    # 插入排序
    # result = insert_sort(list)

    # 希尔排序
    # result = shell_sort(list)

    # 归并排序
    # result=merge_sort(list)

    # 计数排序
    # result=count_sort(list)

    # 桶排序
    # result = bucket_sort(list)

    # 基数排序
    result = radix_sort(list)


    print('排序后：',result)