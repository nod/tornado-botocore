import logging

__version__ = '1.3.1'

try:
    from .base import Botocore
except ImportError:
    logging.warning('It looks like some requirements are missing.')


__all__ = ('Botocore',)
