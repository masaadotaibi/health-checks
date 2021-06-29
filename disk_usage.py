#!/usr/bin/env python

import shutil
import sys

def check_disk_full(disk, min_gb, min_percent):
    """Returns True if therse is enough free disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True

    return False
