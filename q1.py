def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    sequence_str = input("Enter a sequence of positive integers separated by spaces: ")
    sequence = sequence_str.split()
    sequence = [int(num) for num in sequence if num.isdigit()]

    prime_numbers = []
    for num in sequence:
        if is_prime(num):
            prime_numbers.append(num)

    if prime_numbers:
        print("Prime numbers in the sequence:", prime_numbers)
        print("Largest prime number in the sequence:", max(prime_numbers))
    else:
        print("No prime numbers found in the sequence.")

if __name__ == "__main__":
    main()
