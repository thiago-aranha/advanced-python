# Demonstrate how to customize logging output

import logging

# TODO: add another function to log from
def another_function():
    logging.debug("This is a DEBUG message", extra=extData)

# set the output file and debug level, and
# TODO: use a custom formatting specification
fmtStr = "%(user)s %(asctime)s: %(levelname)s: <%(funcName)s> Line:%(lineno)d %(message)s"
dateStr = "%m/%d/%Y %I:%M:%S %p"
extData = {"user": "thiago.aranha"}

logging.basicConfig(filename="output.log",
                    level=logging.DEBUG,
                    format=fmtStr,
                    datefmt=dateStr)

logging.info("This is an info-level log message", extra=extData)
logging.warning("This is a warning-level message", extra=extData)

another_function()
