from typing import Union, Any
import logging

# Configuring logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def generate_factorial_sequence(value: int) -> dict[int, Union[int, Any]]:
    """
    Generate a factorial sequence list up to a specified number of elements

    Args:
        value: The number of factorial numbers to generate.

    Returns:
        List[int]: A list of Factorial numbers up to the specified limit.
    """
    logger.info("Generating Factorial sequence for limit: %d", value)
    sequence = {}
    next_value = 1
    if value == 0:
        sequence[0] = 1
    elif value < 0:
        logger.error("The limit must be at least greater than 0 to generate a valid Factorial sequence.")
        # raise ValueError("The limit must be at least greater than 0 to generate a valid Factorial sequence.")
    else:
        for i in range(1, value+1):
            next_value = next_value*i
            sequence[i] = next_value

        logger.info("Factorial sequence generated: %s", sequence)
    return sequence


if __name__ == "__main__":

    try:
        generate_factorial_sequence(5)  # [1, 2, 6, 24, 120]
        generate_factorial_sequence(-1)
        generate_factorial_sequence(0)
    except ValueError as e:
        logger.exception("Exception occurred: %s", e)
