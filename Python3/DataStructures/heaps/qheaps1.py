import heapq

if __name__ == "__main__":
    heap = []
    for i in range(int(input())):
        nums = list(map(int,input().split()))
        if nums[0] == 1:
            heapq.heappush(heap, nums[1])
        elif nums[0] == 2:
            heap.remove(nums[1])
            heap.sort()
        else:
            print(heap[0])