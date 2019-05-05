"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

import sched
import time
from decimal import Decimal


def schedule(f, milli):
	sleep_time = Decimal(milli) / 1000
	sched.scheduler(time.time, time.sleep).enterabs(sleep_time, 1, f)
