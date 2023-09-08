# demonstrate the logging api in Python

# TODO: use the built-in logging module
import logging

# TODO: Use basicConfig to configure logging
logging.basicConfig(level=logging.DEBUG, filename="output.log")

# TODO: Try out each of the log levels
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")

# TODO: Output formatted strings to the log
