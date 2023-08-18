import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = "C:/Users/tvgge/OneDrive/Área de Trabalho"

class fileEventHandler(FileSystemEventHandler):
    
    def on_created(self, event):
        print(f'ola, {event.src_path} foi criado!')

    def on_deleted(self, event):
        print(f'opa! Alguém excluiu {event.src_path}!')


event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print('executando...')
except KeyboardInterrupt:
    print('interrompido!')
    observer.stop()







