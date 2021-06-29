#!/usr/bin/env python
import os
import sys
import socket
from disk_usage import check_disk_full
from cpu_usage import check_cpu_usage

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")


def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    # Chcek for at least 2 GB and 10% free
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def check_cpu_overloaded():
    """Returns True if the CPU usage is over 75% of its capability"""
    return check_cpu_usage(75)

def check_no_network():
    """Returns True if it fails to resolve Google's URL, False otherwise"""
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True

def main():
    checks = [
        (check_reboot, "Pending Reboot!"),
        (check_root_full, "Root partition is full!"),
        (check_cpu_overloaded, "CPU is overloaded!"),
        (check_no_network, "No working network!")
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
