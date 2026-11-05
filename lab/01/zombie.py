import os, time
pid = os.fork()

if pid == 0:
    os._exit(0)
print(f"filho {pid} morreu, mas o pai nao chamou o wait()")
time.sleep(60)

os.waitpid(pid, 0)


