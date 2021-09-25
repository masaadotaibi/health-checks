#!/usr/bin/env python
import psutil

def check_cpu_usage(percent):
    usage = psutil.cpu_percent(1)
    return usage > percent
