#선택정렬
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index =i
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[i],array[min_index]=array[min_index],array[i]

print(array)

#선택정렬2
def sel_sort(a):
    for i in range(0,len(a)):
        min_idx=i
        for j in range(i+1,len(a)):
            if a[j]<a[min_idx]:
                min_idx=j
        a[i],a[min_idx]=a[min_idx],a[i]

array=[2,4,5,1,3]
sel_sort(array)
print(array)

#삽입정렬
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1): #인덱스 i부터 1ㅅ까지 1씩 감소하며 반복하는 문법
        if array[j]<array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
        else:
            break #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
print(array)

