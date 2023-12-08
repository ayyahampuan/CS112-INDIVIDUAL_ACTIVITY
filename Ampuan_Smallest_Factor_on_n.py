while True:
    num = int(input("\nEnter an integer >= 2 : "))
    if num > 2:
        for i in range(2, num + 1):
            if num % i == 0:
                print("The smallest factor other than 1 for", num, "is", i)
                break
    else:
        print("Invalid input. Try again and enter a number greater than 2.")
        break