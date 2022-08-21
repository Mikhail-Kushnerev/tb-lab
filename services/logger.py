import logging

from utils.constants import DT_FORMAT, LOG_FORMAT


def get_log() -> None:
    logging.basicConfig(
        level=logging.INFO,
        encoding="utf-8",
        format=LOG_FORMAT,
        datefmt=DT_FORMAT,
        handlers=(logging.StreamHandler(),)
    )
