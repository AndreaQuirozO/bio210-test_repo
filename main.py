def print_fibn(n):
    if n < 1:
            print('Invalid number')
            return  

    n_2 = 0
    n_1 = 1

    print(n_2)

    if n == 1:
            return
    
    print(n_1)

    for i in range(2, n):
            n = n_1 + n_2
            print(n)
            n_2 = n_1
            n_1 = n


if __name__ == "__main__":
	n = 10
	print_fibn(n)
