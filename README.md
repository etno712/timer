[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Introduction
============

Library in MicroPython for timers without interrupt:
* Mode one shot or periodic
* The one shot timer can be armed after its instantiation.
* The one shot timer can be rearmed at any time.


Dependencies
=============

This driver has no dependency

Install
=======

Copy the file timer.py in your project folder.

Usage Example
=============

.. code-block:: micropython

    from timer import OneShotTimer, PeriodicTimer

    my_timer = OneShotTimer(3600000) # Time in ms
    while not my_timer.is_activated:
        pass # My work.
    my_timer.start(7200000) # Time in ms
    while not my_timer.is_activated:
        pass # My entertainment.

    my_timer = PeriodicTimer(1000) # Time in ms
    while True:
        if my_timer.is_activated:
            pass # My periodic action

Documentation
=============

Read the code.

Contributing
============

Contributions are welcome!
