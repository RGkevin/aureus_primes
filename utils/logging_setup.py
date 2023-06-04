import logging
import os

from definitions import ROOT_DIR


def logging_setup():
    log_file_name = os.path.join(ROOT_DIR, 'dist/experiment_fibonacci_counter.log')
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file_name),
            logging.StreamHandler()
        ]
    )