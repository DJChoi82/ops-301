#!/bin/python3
#Class 12 Python Script
#DJ Choi
#3/15/2022
#Writing python script to use Psutil

import psutil

#main

#printing what is being output
print("Below are the times in seconds the CPU has spent in a given mode")
#Time spent by normal processes executing in user mode
print("user =",psutil.cpu_times() .user)

#Time spent by processes executing in kernel mode
print("kernel =",psutil.cpu_times() .system)

#Time when system was idle
print("idle =",psutil.cpu_times() .idle)

#Time spent by priority processes executing in user mode
print("prioritzed =",psutil.cpu_times() .nice)

#Time spent waiting for I/O to complete
print("I/O wait =",psutil.cpu_times() .iowait)

#Time spent for servicing hardware interrupts
print("hardware inturrupts =",psutil.cpu_times() .irq)

#Time spent for servicing software interrupts
print("software interrupts =",psutil.cpu_times() .softirq)

#Time spent by other operating systems running in a virtualized environment
print("VM OS =",psutil.cpu_times() .steal)

#Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
print("virtual CPU =",psutil.cpu_times() .guest)

#end
