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

for i in range(1,len(array)): #두번째원소부터시작
    for j in range(i,0,-1): #인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j]<array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
        else:
            break #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
print(array)

#삽입정렬2
def ins_sort(a):
    for i in range(1,len(a)):
        key=a[i] #i번 위치에 있는 값을 key에 저장
        j=i-1 #j를 i바로 왼쪽 위치로 저장
        while j>=0 and a[j]>key: #리스트j번 위치에 있는 값과 key를 비교해 key가 삽입될 적절한 위치를 찾음
            a[j+1]=a[j] #삽입할 공간이 생기도록 값을 오른쪽으로 한칸이동
            j -=1
        a[j+1]=key
array=[2,4,5,1,3]
ins_sort(array)
print(array)

#퀵정렬
array=[7,5,9,0,3,1,6,2,4,8]
def quick_sort(array,start,end):
    if start >=end: #원소가 1개인 경우 종료
        return

    pivot=start #피벗은 첫번째 원소
    left=start+1
    right=end

    while(left<=right):
        #피벗보다 큰 데이터를 찾을때까지 반복
        while(left<=end and array[left]<array[pivot]):
            left +=1
        #피벗보다 작은 데이터를 찾을때까지 반복
        while(right>start and array[right]>=array[pivot]):
            right -=1
        if(left>right): #엇갈렸다면 작은 데이터와 피벗을교체
            array[right],array[pivot]=array[pivot],array[right]
        else: #엇갈리지 않았다면 작은데이터와 큰데이터를 교체
            array[left],array[right]=array[right],array[left]

    #분할이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬수행
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)

#퀵정렬(파이썬의 장점을 살린방식)
array=[7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array)<=1:
        return array
    pivot=array[0] #피벗은 첫번째 원소
    tail=array[1:] #피벗을 제외한 리스트

    left_side=[x for x in tail if x <=pivot] #분할된 왼쪽 부분
    right_side=[x for x in tail if x > pivot] #분할된 오른쪽 부분

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체리스트 반환
    return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(array))

#계수정렬

#모든 원소의 값이 0보다 크거나 같다고 가정
array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
#도든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count=[0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]]+=1 #각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): #리스트에 기록된 정렬정보 확인
    for j in range(count[i]):
        print(i,end='')



    







