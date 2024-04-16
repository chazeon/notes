---
title: Fixing reboot issue due to watchdog
tag: [linux-kernel]
---

Last summer, I acquired a ThinkCentre m900 SFF machine with an i5-6500T processor from eBay for $60, which I set up as a proxy server. Considering that it comes with 4 GB of RAM and 256 GB of SATA SSD, it was a great deal, especially at a time when Raspberry Pi was in shortage and extremely overpriced. I use Arch Linux on this machine. However, I encountered a painful reboot issue that seemed to occur sporadically, primarily after kernel updates. I have to physically reboot it to make it go back to work.

## The issue

The problem arises when `systemd-journald` attempts to send a notification to `WATCHDOG=1`, but fails to do so. This issue doesn't appear to be related to the specific kernel version, as I experienced it with both the Linux and Linux LTS kernels.

```
Apr 16 10:30:02 DESKTOP-xxxxxxx systemd[1]: Stopped Create swap on /dev/zram0.
Apr 16 10:30:02 DESKTOP-xxxxxxx systemd[1]: Removed slice Slice /system/systemd-zram-setup.
Apr 16 10:30:02 DESKTOP-xxxxxxx systemd[1]: lvm2-monitor.service: Deactivated successfully.
Apr 16 10:30:02 DESKTOP-xxxxxxx systemd[1]: Stopped Monitoring of LVM2 mirrors, snapshots etc. using dmeventd or progress polling.
Apr 16 10:30:02 DESKTOP-xxxxxxx systemd[1]: Reached target System Shutdown.
Apr 16 10:30:02 DESKTOP-xxxxxxx systemd[1]: Reached target Late Shutdown Services.
Apr 16 10:30:02 DESKTOP-xxxxxxx systemd[1]: systemd-reboot.service: Deactivated successfully.
Apr 16 10:30:02 DESKTOP-xxxxxxx systemd[1]: Finished System Reboot.
Apr 16 10:30:02 DESKTOP-xxxxxxx systemd[1]: Reached target System Reboot.
Apr 16 10:30:02 DESKTOP-xxxxxxx systemd[1]: Shutting down.
Apr 16 10:30:03 DESKTOP-xxxxxxx systemd[1]: Using hardware watchdog 'iamt_wdt', version 2, device /dev/watchdog0
Apr 16 10:31:28 DESKTOP-xxxxxxx systemd-journald[191]: Failed to send WATCHDOG=1 notification message: Connection refused
```

This last message will repeat constantly until I physically reset the machine. Everything looked fine before `systemd-journald[191]: Failed to send WATCHDOG=1 notification message: Connection refused`, so I believe the watchdogs are causing the issue.

## Inspection

Since this system is Intel-based and has a vPro-enabled CPU, the system is equipped with two watchdogs:

* `iTCO_wdt`
* `iamt_wdt`

After inspecting almost a year of logs, I believe it only occurred when `iamt_wdt` was used. 

Interestingly, the choice between `iTCO_wdt` and `iamt_wdt` seems to be somewhat *random*, possibly determined at compile time. For instance, from December to March, the system primarily used iTCO_wdt, but it switched afterward to `iamt_wdt`.

To see the watchdogs, one can do `ls /dev | grep watchdog`:
```
-> % ls /dev | grep watchdog
watchdog
watchdog0
```

Additionally, to see which watchdog timer modules are loaded, use:
```
-> % lsmod | grep wdt
iTCO_wdt               16384  0
mei_wdt                16384  0
intel_pmc_bxt          16384  1 iTCO_wdt
iTCO_vendor_support    12288  1 iTCO_wdt
mei                   200704  7 mei_wdt,mei_hdcp,mei_pxp,mei_me
```

And to see which watchdog each `/dev/watchdog[0-1]` corresponds to:
```
-> % cat /sys/class/watchdog/watchdog0/identity
iTCO_wdt
```

The `iamt_wdt` is known as `mei_wdt` in the [`mei_wdt.c`][1], which ChatGPT failed to note me.

## Solution

To prevent `iamt_wdt` from interfering with further reboots, I disable it by adding it to the blacklist:
```bash
echo "blacklist mei_wdt" | sudo tee /etc/modprobe.d/mei_wdt.conf
```
After blacklisting, you should see that `mei_wdt` is no longer loaded:
```
-> % lsmod | grep wdt
iTCO_wdt               16384  0
intel_pmc_bxt          16384  1 iTCO_wdt
iTCO_vendor_support    12288  1 iTCO_wdt
```

## Final Thoughts

The above solution should work, I still need to keep using the system to see if I encounter this issue further.

I suspect the issue may be due to potentially corrupted Intel AMT firmware on this machine. I plan to flash the updated AMT firmware soon to verify if this resolves this issue.


[1]: https://github.com/torvalds/linux/blob/master/drivers/watchdog/mei_wdt.c