"""Objets connectés | Extension voir-ma-photo"""

from os import path
import functools
import signal
import sys
import time

sys.path.append(path.join(path.dirname(path.abspath(__file__)), 'lib'))

from pkg.voir_ma_photo_handler import VoirMaPhotoHandler  # noqa


_HANDLER = None

print = functools.partial(print, flush=True)


def cleanup(signum, frame):
    """Clean up any resources before exiting."""
    if _HANDLER is not None:
        _HANDLER.close_proxy()

    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)
    _HANDLER = VoirMaPhotoHandler(verbose=True)

    # Wait until the proxy stops running, indicating that the gateway shut us
    # down.
    while _HANDLER.proxy_running():
        time.sleep(2)
