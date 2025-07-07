def determine_output(number):

    result = str(number)
    
    # Check if divisible by both 3 and 5 (must be checked first)
    if number % 3 == 0 and number % 5 == 0:
        result += " fizzbuzz"
    # Check if divisible by 3
    elif number % 3 == 0:
        result += " fizz"
    # Check if divisible by 5
    elif number % 5 == 0:
        result += " buzz"
    
    return result

def main():

    for i in range(1, 101):
        output = determine_output(i)
        print(output)

if __name__ == "__main__":
    main()