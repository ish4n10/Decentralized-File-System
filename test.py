import subprocess
import threading

def run_file(filename):
    subprocess.run(["python", filename])

thread1 = threading.Thread(target=run_file, args=("peer.py",))
thread2 = threading.Thread(target=run_file, args=("run_app.py",))

thread1.start()
thread2.start()
