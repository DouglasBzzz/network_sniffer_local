import subprocess, os, threading, time

from queue import Queue

lock = threading.Lock()

_start = time.time()

def check(n):
    with open(os.devnull, "wb") as limbo:
        ip = f"192.168.2.{n}"
        result = subprocess.Popen(["ping", "-n", "1", "-w", "300", ip],
                                  stdout=limbo, stderr=limbo).wait()
        with lock:
            if not result:
                print(ip, "ativo")
            else:
                print(ip, "inativo")

def threader():
    while True:
        worker = q.get()
        check(worker)
        q.task_done()
q = Queue()

for x in range(255):
    t = threading.Thread(target=threader)
    t.daemon=True
    t.start()

for worker in range(1,255):
    q.put(worker)
q.join()

print(f"Processamento completo: {time.time()-_start}")