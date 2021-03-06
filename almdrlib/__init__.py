__version__ = '1.0.23'
__author__ = 'Alert Logic, Inc.'

import logging
from almdrlib.session import Session

IWS_DEFAULT_SESSION = None


def set_logger(name='almdrlib', level=logging.DEBUG, format_string=None):
    """
    Add a stream handler for the given name and level to the logging module.
    By default, this logs all almdrlib messages to ``stdout``.

        >>> import almdrlib
        >>> almdrlib.set_logger('almdrlib.client', logging.INFO)

    For debugging purposes a good choice is to set the stream logger to ``''``
    which is equivalent to saying "log everything".

    :type name: string
    :param name: Log name
    :type level: int
    :param level: Logging level, e.g. ``logging.INFO``
    :type format_string: str
    :param format_string: Log message format
    """

    if format_string is None:
        format_string = "%(asctime)s %(name)s [%(levelname)s] %(message)s"

    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    handler.setLevel(level)
    formatter = logging.Formatter(format_string)
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def _get_default_session():
    global IWS_DEFAULT_SESSION
    if not IWS_DEFAULT_SESSION:
        IWS_DEFAULT_SESSION = Session()
    return IWS_DEFAULT_SESSION


def client(service_name, version=None, session=None, *args, **kwargs):
    if session is None:
        session = _get_default_session()
    return session.client(service_name, version, *args, **kwargs)


# Logging to dev/null
# http://docs.python.org/3.3/howto/logging.html#configuring-logging-for-a-library
class NullHandler(logging.Handler):
    def emit(self, record):
        pass


logging.getLogger('almdrlib').addHandler(NullHandler())
