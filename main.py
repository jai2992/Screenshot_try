import time
from watchdog.observers.polling import PollingObserver as Observer
from utils.listner import ImageHandler

def main():
        event_listner = ImageHandler()
        observer = Observer()
        observer.schedule(event_listner, "./image", recursive = False)
        observer.start()
        while True:
            time.sleep(1)
        observer.join()
if __name__ == "__main__":
    print("app started")
    main()
