#Import UCS modules
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.utils.ucsbackup import backup_ucs
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", help="IP Address")
parser.add_argument("-u", "--username", help="Username")
parser.add_argument("-p", "--password", help="Password")

args = parser.parse_args()

#Log into UCS using UcsHandle
handle = UcsHandle(ip=args.ip, username=args.username, password=args.password, secure=False)
handle.login()

#Start backup scripts here
backup_dir = "c:\ucsbackup"
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
