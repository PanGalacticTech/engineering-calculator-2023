




def percentage_difference(a, b):
    difference = a - b
    average = (a+b)/2
    pc_diff = round((difference/average)*100, 3)
    print(f"Number A: {a}, Number B: {b} ")
    print(f"Percentage Difference = {pc_diff} %")
    return pc_diff


percentage_difference(5, 6)