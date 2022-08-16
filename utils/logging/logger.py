import sys
from loguru import logger


def setup_logger(logger_level: str):
    logger.remove()
    format_log = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> " \
                 "|| <level>{level}</level>: " \
                 "{message}\t" \
                 "<r><<module:{module}__func:{function}__line:{line}>></r> || \n" \
                 "<y>payload={extra}</y>"

    logger.add(sink=sys.stdout, level=logger_level, format=format_log, colorize=True, backtrace=True, diagnose=True)
