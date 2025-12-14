import os
from watchdog.events import FileSystemEventHandler

class ImageHandler(FileSystemEventHandler):

    def on_created(self, event):

        # Do nothing if it is a directory
        if event.is_directory:
            return None
        
        # Get the filename and extension
        filename, extension = os.path.splitext(event.src_path)

        valid_extension = ['.jpg', '.jpeg', '.png']

        if extension not in valid_extension:
            return None

        print("New Image Found", event.src_path)

