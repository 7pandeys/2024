"""This module provides a function to check if the number is prime or not."""

def prime_numbers(x: int) -> str:
    """
    Determine if a number is prime.

    Args:
        x (int): The number to check for primality

    Returns:
        str: A message stating whether the number is prime or not.

    """
    for i in range(2,x//2+1):
        if x%i == 0:
            return f"{x} is Not Prime Number"
    return f"{x} is Prime Number"



if __name__ == "__main__":
    for n in [10,11]:
        s = prime_numbers(n)
        print(s)
