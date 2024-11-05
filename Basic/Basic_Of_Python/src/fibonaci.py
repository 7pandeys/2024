from typing import List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def generate_fibonacci_sequence(limit: int) -> List[int]:
    """
    Generate a fibonacci sequence list up to a specified number of elements

    Args:
        limit: The number of fibonacci numbers to generate. Must be at least 2.

    Returns:
        List[int]: A list of Fibonacci numbers up to  the specified limit.
    """
    if limit < 2:
        logger.error("The limit must be at least 2 to generate a valid Fibonacci sequence.")
        raise ValueError("The limit must be at least 2 to generate a valid Fibonacci sequence.")

    logger.info("Generating Fibonacci sequence for limit: %d", limit)

    # Initialize the first two Fibonacci numbers
    first, second = 0, 1
    sequence = [first, second]

    # Generate the Fibonacci sequence up to the specified limit
    for _ in range(2, limit):
        next_value = first + second
        sequence.append(next_value)
        logger.debug("Generated next Fibonacci number: %d", next_value)
        first, second = second, next_value


    logger.info("Fibonacci sequence generated: %s", sequence)
    return sequence


if __name__ == "__main__":
    try:
        print(generate_fibonacci_sequence(1)) # Output: [0, 1, 1, 2, 3]
    except ValueError as e:
        logger.exception("Exception occurred: %s", e)

