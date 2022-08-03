import sys
from loguru import logger
from settings import LOGGER_LEVEL


def setup_logger():
    logger.remove()
    format_log = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> " \
                 "|| <level>{level}</level>: " \
                 "{message}\t" \
                 "<r><<module:{module}__func:{function}__line:{line}>></r> || " \
                 "<y>paylod={extra}</y>"

    logger.add(sink=sys.stdout, level=LOGGER_LEVEL, format=format_log, colorize=True, backtrace=True, diagnose=True)
