#!/usr/bin/env python
import os
import sys
from disk_usage import check_disk_full

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")


def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    # Chcek for at least 2 GB and 10% free
    return check_disk_full(disk="/", min_gb=2, min_percent=10)


def main():
    checks = [
        (check_reboot, "Pending Reboot"),
        (check_root_full, "Root partition is full"),
    ]

    everything_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False

        if not everything_ok:
            sys.exit(1)

    print("Everything ok.")
    sys.exit(0)

main()
