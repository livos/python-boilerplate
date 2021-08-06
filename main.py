#!/usr/bin/env python3

import argparse
import logging
from typing import Any

from app import math

logger = logging.getLogger(__name__)


def configure_logging() -> None:
    root_logger = logging.getLogger()

    c_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s %(name)-15s %(levelname)-4s %(message)s",
        "%Y-%m-%d %H:%M:%S",
    )
    c_handler.setFormatter(formatter)

    f_handler = logging.FileHandler("app.log", mode="a")
    f_handler.setFormatter(formatter)

    root_logger.addHandler(c_handler)
    root_logger.addHandler(f_handler)
    root_logger.setLevel(logging.INFO)


def main(_: Any) -> None:
    configure_logging()
    logger.info("Started runnning")
    print(math.multiply_two_numbers(5, 8))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Boilerplate",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    main(parser.parse_args())
