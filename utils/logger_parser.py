import logging


def logger_parser(context, msg, params=None):
    if params is None:
        params = []

    end_msg = msg.format(*params)
    logging.info('{}:: {}'.format(context, end_msg))
