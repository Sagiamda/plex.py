import logging

log = logging.getLogger(__name__)

__version__ = '0.6.3'


try:
    from plex.client import Plex
except Exception as ex:
    log.warn('Unable to import submodules - %s', ex, exc_info=True)
