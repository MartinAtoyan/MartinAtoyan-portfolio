import threading
import time
import queue


log_queue = queue.Queue()

log_file_path = "server_log.txt"

def log_reader():
    file = open(log_file_path, 'r')
    file.seek(0, 2)

    while True:
        line = file.readline()
        if line:
            log_queue.put(line)
        else:
            time.sleep(0.1)

def error_detector():
    while True:
        try:
            line = log_queue.get(timeout=1)
            if "ERROR" in line:
                print(f"Error detected: {line.strip()}")
        except queue.Empty:
            continue

reader_thread = threading.Thread(target=log_reader, daemon=True)
detector_thread = threading.Thread(target=error_detector, daemon=True)

reader_thread.start()
detector_thread.start()

reader_thread.join()
detector_thread.join()


