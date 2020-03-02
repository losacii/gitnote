## SHUTDOWN, 360 seconds, power on
sudo rtcwake -m off -s 360

## SLEEP, after 30 seconds, wake up
sudo rtcwake -m mem -s 30

## specific time
sudo rtcwake -m mem --date 2019-10-25 08:00
sudo rtcwake -m mem --date 2019-10-29 07:50

## tomorrow 6:30
sudo rtcwake -m no -l -t $(date +%s -d ‘tomorrow 06:30’)

## Follow a command
rtcwake -m mem -s 120 && firefox


## Types of Suspend

The -m switch accepts the following types of suspend:

standby – Standby offers little power savings, but restoring to a running
system is very quick. This is the default mode if you omit the -m switch.

mem – Suspend to RAM. This offers significant power savings – everything is put
into a low-power state, except your RAM. The contents of your memory are
preserved.

disk – Suspend to disk. The contents of your memory are written to disk and
your computer is powered off. The computer will turn on and its state will be
restored when the timer completes.

off – Turn the computer off completely. rtcwake’s man page notes that restoring
from “off” isn’t officially supported by the ACPI specification, but this works
with many computers anyway.

no – Don’t suspend the computer immediately, just set the wakeup time. For
example, you could tell your computer to wake up at 6am. After that, can put it
to sleep manually at 11pm or 1am – either way, it will wake up at 6am.
