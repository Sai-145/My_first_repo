def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Get user input
number = int(input("Enter a number: "))

# Calculate factorial
factorial_result = factorial(number)
print(f"The factorial of {number} is {factorial_result}")

# Check if the number is prime
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.)

        "Hi this is the added code of pyhton"
