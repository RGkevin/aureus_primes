import sys
from datetime import datetime

from utils.logger_parser import logger_parser


def end_experiment(start_time, exp_name):
    later_time = datetime.now()
    delta_time = (later_time - start_time).total_seconds()
    logger_parser('ENDED EXPERIMENT' + exp_name, ':: took {} seconds', [delta_time])
    sys.exit()
