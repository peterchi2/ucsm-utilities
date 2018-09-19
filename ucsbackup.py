#Import UCS modules
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.utils.ucsbackup import backup_ucs


#Log into UCS using UcsHandle
handle = UcsHandle("10.10.20.113", "ucspe", "ucspe", secure=False)
handle.login()

#Start backup scripts here
backup_dir = "/home/user/backup"
full_state_backup_filename = "full-state_config_backup.xml"
backup_ucs(handle,
           backup_type = "full-state",
           file_dir = backup_dir,
           file_name = full_state_backup_filename)

config_all_backup_filename = "config-all_config_backup,xml"
backup_ucs(handle,
           backup_type = "config-all",
           file_dir = backup_dir,
           file_name = config_all_backup_filename,
           preserve_pooled_values = True)

#Log out of UCS
handle.logout()
