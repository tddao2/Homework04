#1954347
#Tri Dao
#14.11 CIS 2348 LAB Descending selection sort with output during execution

# TODO: Write a selection_sort_descend_trace() function that 
#       sorts the numbers list into descending order
def selection_sort_descend_trace(numbers):
   for i in range(len(numbers) - 1):
        # Find index of smallest remaining element
        index_smallest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[index_smallest]:
                index_smallest = j
        # Swap numbers[i] and numbers[index_smallest]
        temp = numbers[i]
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp
        
        for num in numbers:
            print(str(num), end=' ')
        print()

if __name__ == "__main__":
    # TODO: Read in a list of integers into numbers, then call
    #       selection_sort_descend_trace() to sort the numbers
    numbers = [int(num) for num in input("").split()] 
    selection_sort_descend_trace(numbers)
    
#Referrences
#14.6 Selection sort