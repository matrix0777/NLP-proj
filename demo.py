from hate.logger import logging
from hate.exception import CustomException
import sys

""" logging.info("This is an info message") """

try:
    a = 1 / '0'
except Exception as e:
    raise CustomException(e, sys) from e
    logging.error("Error occurred while dividing by zero: %s", e)