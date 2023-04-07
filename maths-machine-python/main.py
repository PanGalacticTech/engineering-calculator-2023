

'''

 So I hate doing boring low level number conversions, and python has a suite of built in tools
 to help convert from one number format to others.

 But in this case we cannot "show our workings" to use the answer in our homework.

 So instead I have written everything the "verbose" way so the output of each script can be copied
 directly into your homework - showing your exact working and getting full marks!

 Good luck. Make sure to source this properly or it's cheating!

 Imogen Wren, 2023

'''

import complex_numbers as cm
import percentages as pc
import matrices as mx
import matplotlib




def decimal_binary(decimal_int, min_len=4):
    binary_list = []
    new_val = decimal_int
    while new_val > 0:
        remainder = new_val % 2
        new_val = int(new_val / 2)
        #binary_list.append(remainder)
        binary_list.insert(0, remainder)  ## Insert at the front of the list
        print(f"Initial Int: {decimal_int}, new_val: {new_val}, remainder:{remainder}, binary:{binary_list}")
        decimal_int = new_val
    print("Binary Out:")
    length = len(binary_list)
    #print(f"\nlength: {length}")
    while length % min_len != 0:
        binary_list.insert(0, 0)
        length = len(binary_list)
    for i in binary_list:
        print(i, end="")
    print("\n")
    return binary_list


bin_lookup = ["000", "001", "010", "011", "100", "101", "110", "111"]   ## lookup table for 8 characters

def octal_binary(octal_int):
    print(f"Initial Octal: {octal_int}")
    binary_list = []
    # Seperate each digit in octal
    oct_string = str(octal_int)
    oct_list = []
    for i in oct_string:
        oct_list.append(int(i))
    print(f"List Digits: {oct_list}")
    # Convert each digit to 3 digit binary
    for j in oct_list:
        print(f"Digit: {j}, Binary: {bin_lookup[j]}")
        binary_list.append(bin_lookup[j])
    print("Binary Out: ")
    for i in binary_list:
        print(i, end="")
    print("\n")
    return binary_list

## Cut a string into n sized chunks and return as list
def chunks(string, n):
    chunk_list = []
    for i in range(0, len(string), n):
        #print(string[i:i + n])
        chunk_list.append(string[i:i + n])
    return chunk_list

def reversed_string(a_string):
    return a_string[::-1]

def binary_decimal(binary_str):
    print(F"Initial Binary: {binary_str}")
    j = len(binary_str)-1     #
    decimal = 0
    for i in binary_str:
        print(f"{int(i)}", end="")
        decimal = decimal + (2**j)*int(i)    ## ** = ^
        j = j-1
    print(f"\nDecimal Out: {decimal}")
    return decimal



def binary_octal(binary_str):             ## Pass binary as a string
    #Ensure that binary string has enough characters to split into 3 bit chunks
    octal_list = []
    print(f"Initial Binary: {binary_str}")
    length = len(binary_str)
    print(f"length: {length}")
    while length % 3 != 0:
        binary_str = "0" + binary_str
        length = len(binary_str)
    print(f"Octalised Binary: {binary_str}")
    print(f"length: {length}")
    ## Split the binary string into 3 bit chunks
    binary_chunks = chunks(binary_str, 3)
    print(f"List of Octal Binary Chunks: {binary_chunks}")
    for i in binary_chunks:
        octal_list.append(binary_decimal(i))
    print("Octal Out: ")
    for i in octal_list:
        print(i, end="")
    print("\n")
    return octal_list

hex_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8" ,"9","A","B","C","D", "E", "F", "NULL"]

hex_list = ["B0A", "B05", "B00"]

def hex_decimal(hex_list):
    list_num = 0
    for i in (hex_list):
        decimal_total = 0
        print(f"Initial Hex {list_num}: {i}")
        # First string must be reversed so LSB is processed first
        r_hex_string = reversed_string(i)
        print(f"Reversed hex String: {r_hex_string}")
        char_num = 0 # Iteration variable, will be used for labelling and as a power of 16
        for j in r_hex_string:
            k = 0
            print(f"hex 16^{char_num}: {j}")
            while hex_chars[k] != j.upper():
                k = k + 1  ## Increment through the list untill a match is found
            print(f"Decimal 16^{char_num}: {k}")  ## Whichever increment was landed on is the decimal for the hex character
            # This must be multiplied by 16 to the power of char_num
            value = int(k)*(16**char_num)
            print(f"Decimal Value: {value}")
            decimal_total = decimal_total + value
            char_num += 1
        print(f"\nDecimal {list_num} Total = {decimal_total}\n")
        list_num += 1

def hex_binary(hex_str):
    binary_list = []
    print(f"Initial Hex: {hex_str}")
    for i in hex_str:
        j = 0
        print(f"hex: {i}")
        while hex_chars[j] != i.upper():
            j = j+1    ## Increment through the list untill a match is found
        print(f"Decimal: {j}")  ## Whichever increment was landed on is the decimal for the hex character
        binary_list.append(decimal_binary(j))
    print("Binary Out:")
    for k in binary_list:
        for l in k:
            print(l, end="")
    return binary_list





def decimal_hex(decimal_int):
    print(F"Initial Decimal: {decimal_int}")
    hex_str_list = []
    new_val = decimal_int
    while new_val > 0:
        remainder = new_val % 16
        print(f"Remainder: {remainder}")
        new_val = int(new_val / 16)
        # binary_list.append(remainder)
        hex_str_list.insert(0, hex_chars[remainder])  ## Insert at the front of the list
        print(f"Initial Int: {decimal_int}, new_val: {new_val}, remainder:{remainder}, hex:{hex_str_list}")
    print("Hex Out: ")
    for i in hex_str_list:
        print(i, end="")
    return hex_str_list







def decimal_to_gray_op(n):
   #n = int(n, 2)
   n ^= (n >> 1)
   grey = bin(n)[2:]
   grey_s = str(grey)
   while len(grey_s) < 4:
       grey_s = "0" + grey_s
   return grey_s




A = [[ 1, 7, 1 ],
     [13, 9, 2]]

C = [[3, 6],
     [0, 0],
     [2, 1]]

B = [[1, 14],
     [0, 5]]


def main():
     #for n in range(0, 16):
     #   print(decimal_to_gray_op(n))
    mx.return_rows_columns(A)
    print("\n")
    mx.print_matrix(A)
    print("\n")
    mx.return_n_column(A, 0)
    print("\n")
    mx.return_n_row(A, 1)
    print("\n")
    mx.return_determinant(B)
    print("\n")
    B_inversion = mx.invert_matrix(B)
    print("\n")
    mx.matrix_dot_matrix(B, B_inversion)

    #pc.percentage_difference(100, 102.5)
    #cm.complex_num_main()
    #decimal_hex(binary_decimal("100011100011"))
    #decimal_hex(2806)
    #hex_decimal(hex_list)


    #hex_binary("128")
    #binary_octal("11100011")
    #binary_decimal("101110")

    #octal_binary(125)
    #decimal_binary(45)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
