number_list: list = [50,8,-50,10.45,100054]

def order_list(numbers: list) -> list:
    new_number_list = numbers.copy()

    for i in range(len(new_number_list)):
        for j in range(i+1, len(new_number_list)):
            if new_number_list[i] > new_number_list[j]:
                new_number_list[i], new_number_list[j] = new_number_list[j], new_number_list[i] 
    return new_number_list

new_list= order_list(number_list)
print(new_list)
