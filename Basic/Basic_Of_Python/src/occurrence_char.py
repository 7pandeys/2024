"""This module is to check occurances of character."""

import argparse
import logging


# from Basic
# from .configs.occurrence_config import (INPUT_STRING)


def count_of_occurrence(value):
    """
    Determine if a number is prime.

    Args:
        x (int): The number to check for primality

    Returns:
        str: A message stating whether the number is prime or not.

    """
    d = {}
    for i in value:
        if i not in d:
            d[i] = + 1
        else:
            d[i] = 1
    return d


class OccurrenceChar:
    """HelloArg."""

    def __init__(self):
        """
        Get Instance of OccurrenceCharacter.

        :param logger: Logger
        :param input_string: input value
        """
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s = %(message)s')
        self.logger = logging.getLogger(__name__)

        self.parser = argparse.ArgumentParser(description="Occurrence of Characters")
        self.parser.add_argument('--verbose', action='store_true', help='Enable verbose logging')
        self.parser.add_argument('--name', type=str, required=True, help="String to be process")

    def parse_arguments(self):
        """
        Determine if a number is prime.

        Args:
            x (int): The number to parse arguments

        Returns:
            str: arguments.

        """
        args = self.parser.parse_args()
        if args.verbose:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)
        return args

    def run(self):
        """
        Determine if a number is prime.

        Args:
            x (int): The number to check for primality

        Returns:
            str: A message stating whether the number is prime or not.

        """
        args = self.parse_arguments()
        self.logger.debug('Arguments parsed: %s', args)

        # Example of using the parsed argument
        self.logger.info('Hello, %s!', args.name)

        # Simulate some processing
        try:
            self.logger.debug('Starting processing...')
            # Simulate processing step
            out = count_of_occurrence(args.name)
            # result = f"Output {out}"
            self.logger.info("Here you GO :")
            for key, value in out.items():
                self.logger.info("%s is occurring %s times", key, value)

            # self.logger.info('Processing complete: %s', result)
        except (TypeError, KeyError) as e:
            self.logger.error('A specific error occurred: %s', e)


if __name__ == "__main__":
    app = OccurrenceChar()
    app.run()
