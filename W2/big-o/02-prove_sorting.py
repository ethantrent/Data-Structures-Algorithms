def sort_list(data):
    for sort_pos in range(len(data)-1, 0, -1):
        for swap_pos in range(0, sort_pos):
            if data[swap_pos] > data[swap_pos+1]:
                data[swap_pos], data[swap_pos+1] = data[swap_pos+1], data[swap_pos]
        
numbers = [3,2,1,6,4,9,8]
sort_list(numbers)
print(numbers)  #[1, 2, 3, 4, 6, 8, 9]