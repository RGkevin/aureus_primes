import sys
from datetime import datetime


def end_experiment(start_time, exp_name):
    later_time = datetime.now()
    delta_time = (later_time - start_time).total_seconds()
    print('ENDED EXPERIMENT:: {} took {} seconds'.format(exp_name, delta_time))
    sys.exit()
