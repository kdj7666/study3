indexing : 리스트내에서 위치값으로 원하는 요소 추출하기
indexing = [1,2,3,4,5]
print(indexing)   # [1,2,3,4,5]
print(indexing[0])   # 1
print(indexing[0]+indexing[-1])   # 6 => 1+5
indexing = [1,2,3, ['a','b','c']]
print(indexing[0])   # 1
print(indexing[3])   # ["a", "b", "c"]
print(indexing[3][-1])   # c

# slicing : 리스트내에서 위치값으로 원하는 가져오기 
slicing = [1, 2, 3, [ 'a', 'b', 'c'], 4, 5]
print(slicing[2:4]) 
# 리스트 값 수정하기
a = [1,2,3]
a[2] = 4
print(a)

# 리스트 값 삭제하기(del)
a = [1,2,3,4,5,6,7,8,9,10]
del a[9] # 9번째 리스트 값 삭제 
print(a) # [1,2,3,4,5,6,7,8,9]
del a[3:] # 3번째자리수 이후 모두 삭제 
print(a) # [1,2,3]

# 리스트 값 추가하기  ( append, extend )
a = [1,2,3,4,5]
a.append(6) # 리시트 a에 요소로 6을 넣음 
print(a)    # [1,2,3,4,5,6]
a.append([7,8,9,10]) 
print(a)  #  [ 1,2,3,4,5,6 [7,8,9,10]]
b = [1,2,3,4,5]
b.extend(['a', 'b', 'c', 'd'])
print(b) # [1,2,3,4,5 'a', 'b', 'c', 'd',]

# 리스트 정렬 ( sort )
a = [1,4,3,2,5]
print(a) # [1,4,3,2,5]
a.sort() # 오른차순 정렬
print(a) # [1, 2, 3, 4, 5]

# 리스트 뒤집기 ( reverse )
a = ['a', 'b', 'c', 'z', 'f', 'i']
a.reverse()
print(a) # ['i', 'f', 'z', 'c', 'b', 'a']

# 리스트 요소 삽입 ( insert )
a = [1,2,3]
a.insert(0,10)
print(a)

# 리스트 요소 제거 ( remove ) : 첫번째로 나오는 요소를 삭제해줌 
a = [1,2,3,1,2,3]
a.remove(3) # 리스트에서 첫번째로 나오는 3을 삭제 
print(a)

# 리스트 요소 끄집어 내기 ( pop ) 
# 마지막 요소를 꺼내주고 기존 리스트에서 해당 요소를 삭제
a = [1,2,3]
print(a) # [1,2,3]
a.pop() # 맨 뒤에 요소 1개 [3]를 끄집어 냄 
print(a) # [1,2]
a.pop() # 맨 뒤에 요소 1개 [2]를 끄집어 냄
print(a) 
a.pop() # 맨 뒤에 요소 1개(1)를 끄집어 냄
print(a) # []

# 리스트에 포함된 요소 x의 개수 세기(count)
a = [1,2,3,1]
b = ['a', 'b', 'c', 'a', 'd', 'e', 'a']
print(a.count(1)) # 2 -> a 리스트에 1이 2개 있음
print(b.count('a')) # 3 -> b 리스트에 a가 3개 있음

# 튜플 기본
tuple1 = ()
tuple2 = (1,)
tuple3 = (1,2,3)
tuple4 = 1,2,3
tuple5 = ('a', 'b', ('ab', 'cd', ('xyz',)))
