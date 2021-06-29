#!/usr/bin/env python
import os
import sys
from disk_usage import check_disk_full

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")


def check_root_usage():
    """Returns True if the root partition is full, False otherwise."""
    # Chcek for at least 2 GB and 10% free
    return check_disk_full(disk="/", min_gb=2, min_percent=10)


def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)

    if check_root_usage():
        print("Root partition full!")
        sys.exit(1)

    print("Everything ok.")
    sys.exit(0)

main()
