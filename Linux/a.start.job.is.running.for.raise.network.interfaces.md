# Code:
sudo nano /etc/systemd/system/network-online.target.wants/networking.service
# Change Code:
TimeoutStartSec=5min
# to Code:
TimeoutStartSec=1sec

then, your computer will boot faster!



sudo vim /etc/systemd/user.conf

DefaultTimeoutStartSec=1s
DefaultTimeoutStopSec=1s
DefaultRestartSec=100ms

sudo systemctl daemon-reload
sudo reboot
