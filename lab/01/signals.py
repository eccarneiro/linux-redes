import os, signal, time

def handler(signum, frame):
    print(f"Recebi o sinal {signal.Signals(signum).name}")
    if signum == signal.SIGINT or signum == signal.SIGTERM:
        print("Vou encerrar o processo e sari limpando os recursos")
        raise SystemExit(0)

signal.signal(signal.SIGINT, handler) # Ctrl + C
signal.signal(signal.SIGTERM, handler) # Kill <pid>
signal.signal(signal.SIGHUP, handler) # kill -HUP <pid> (recarregar config)
signal.signal(signal.SIGUSR1, handler) # sinal livre para a aplicação


print(f"PID {os.getpid()} — teste: kill -USR1 {os.getpid()}  /  kill {os.getpid()}  /  kill -9 {os.getpid()}")
while True:
    time.sleep(1)