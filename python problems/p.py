#count how many times a number appear 
#arr = [2, 3, 3, 3, 2, 5, 1]
#count = 0
#for num in arr:
    #if num == 3:
        #count+=1
#print(count)

#find the largest number
#arr = [4, 5, 1, 7, 3]
#largest = arr[0]
#for num in arr:
    #if num > largest :
        #largest = num 
#print(largest)

#first duplicate element 
#arr = [1, 2, 3, 2, 5]
#for i in range(len(arr)):
    #for j in range(i + 1, len(arr)):
        #if arr[i] == arr[j]:
            #print(arr[i])
            #break

#reverse a list 
#list = [1, 2, 3, 4]
#reversed_list = []
#for i in range(len(list)-1, -1, -1):
    #reversed_list.append(list[i])
    #print(reversed_list)

#find second largest number 
#arr = [2, 3, 4, 5, 6, 7, 9]
#def second_largest(arr):
    #largest = float('-inf')
    #second = float ('-inf')
    #for num in arr:
        #if num > largest:
            #second = largest
            #largest = num
        #elif num > second and num != largest:
            #second = num 
    #return second
#print(second_largest(arr))

#count frequency of elements
#list = [1, 2, 2, 3, 1, 1]
#freq = {}

#for num in list:
    #if num in freq:
        #freq[num] += 1
    #else:
        #freq[num] = 1
#print(freq)
  

#checki if duplicates exists 
#arr = [1, 2, 3, 1, 2]
#seen = set()
#duplicate_found = False

#for num in arr:
    #if num in seen:
        #duplicate_found = True
        #break
    #seen.add(num)
#print(duplicate_found)

#find the missing number 
#arr = [1, 2, 4, 5]
#def find_missing(arr, n):
 #   expected_sum = n * (n + 1 ) // 2
  #  actual_sum = sum(arr)

   # return expected_sum - actual_sum
#print(find_missing(arr, 5))

#first non-repeating element
#arr = [4, 5, 1, 2, 0, 4]
#def first_non_repeating(arr):
    #freq = {}
    #for num in arr:
     #   freq[num] = freq.get(num, 0) + 1

    #for num in arr:
       # if freq[num] == 1:
      #      return num
        
     #   return -1
    #print(first_non_repeating(arr))

#move all zeroes to the end 
#arr = [0, 1, 0, 3, 12]
#def move_zeros(arr):
 #   result = []

  #  for num in arr:
   #     if num != 0:
    #        result.append(num)
    #zeros = len(arr) - len(result)
    #result.extend([0] * zeros)

    #return result
#print(move_zeros(arr))

#two sum problem 
arr = [2, 7, 11, 15]
def two_sum(arr, target):
    seen = set()

    for num in arr:
        needed = target - num

        if needed in seen:
            return [needed, num]
        
        seen.add(num)
        return []
print(two_sum(arr, 9)) 