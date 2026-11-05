import os, time


print(f"[pai] PID={os.getpid()} PPID={os.getppid()}")

pid = os.fork()
if pid == 0:
    print(f"[Filho] PID={os.getpid()} PPID={os.getppid()}")
    time.sleep(1)
    os._exit(7)

else:
    print(f"[Pai] criei o filho {pid}, esperando....")
    _, status = os.waitpid(pid, 0)
    print(f"[Pai] Filho terminou com código {os.waitstatus_to_exitcode(status)}")