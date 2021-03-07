import os

from MyGUI.controller.executor import execute


def put_pc_to_sleep() -> None:
    bash_command = "systemctl suspend"
    execute(bash_command)


def logout_user() -> None:
    data_file = "./helper_files/whouser.txt"
    bash_command = f"who -u >> {data_file}"
    execute(bash_command)

    with open(data_file, "r") as file:
        username = file.readline().split()[0]
    bash_command = f"sudo -A pkill -KILL -u {username}"

    os.remove(data_file)
    execute(bash_command)


def shutdown() -> None:
    bash_command = "shutdown"
    execute(bash_command)


def cancel_shutdown() -> None:
    bash_command = "shutdown -c"
    execute(bash_command)
