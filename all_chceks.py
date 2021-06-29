#!/usr/bin/env python
import os
import sys
from disk_usage import check_disk_usage

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)

    # Chcek for at least 2 GB and 10% free
    if check_disk_usage(disk="/", min_gb=2, min_percent=10):
        print("Disk full!")
        sys.exit(1)

    print("Everything ok.")
    sys.exit(0)

main()
