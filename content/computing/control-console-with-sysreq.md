Date: 2011-12-28 01:12
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Control Console with SysReq
Slug: control-console-with-sysreq
Tags: cli,linux,sysreq,console,computing
Ads: bottom

System request (often abbreviated SysRq or Sys Req) is a key on keyboards for PCs that has no standard use. This key can be traced back to the operator interrupt key of the IBM System/370 mainframe computer. But under Linux there's a bunch of useful things available via this key.




>Note that this is documented only on i386 on Linux, and the kernel must be compiled with the "Magic SysRq Key" option. Find out if it has been by looking at /proc/sys/kernel/sysrq and seeing if that file contains '1'.




#Method

Press `Alt-Sysreq` followed by one of the following letters:



|Key|Result|

|-----|-----|

|r|Unraw: Restores the keyboard after an X crash or similar.|

|0|Changes console loglevel to 0 and so reduces error messages.|

|k|System attention key: Kills all processes on the current virtual console.|

|e|Terminate: Kills all processes except init on the current terminal.|

|i|Kill: Kills all processes except init, everywhere.|

|s|Sync: Attempts to sync all mounted filesystems. Outputs OK and Done when it's managed. This can reduce the chances of needing to run fsck at a later stage so it can be useful if you're having disk problems.|

|u|Umount: Attempts to remount all mounted filesystems read-only.|

|b|Reboot: immediately reboots the system without syncing or unmounting disks. Not a good idea unless in extremis! This may lead to data loss.|

|p|Dumps current registers and flags to the console.|

|m|Dumps current memory info to the console.|









