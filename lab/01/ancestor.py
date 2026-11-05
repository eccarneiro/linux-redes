import os, subprocess

current_pid = os.getpid()
current_ppid = os.getppid()

while current_ppid != 1:
    try:
        print(f"PID {current_pid} é filho de PID {current_ppid}")

        current_pid = current_ppid

        current_ppid = int(
            subprocess.check_output(
                ["ps", "-o", "ppid=", "-p", str(current_pid)],
                text=True
                ).strip()
            )
    except subprocess.CalledProcessError:
        print(f"PID {current_pid} não foi possivel encontrar o PPID, provavelmente o processo já terminou")
        break
else:   
    print(f"PID {current_pid} é filho de PID {current_ppid} (init)")