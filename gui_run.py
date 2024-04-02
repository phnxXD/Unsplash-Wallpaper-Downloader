import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from string import ascii_letters, digits
from random import choice
from os import system, name
from time import sleep
from requests import get

script_version = '1.0'
script_title = 'Unsplash WP Downloader by ALIILAPRO (version {})'.format(script_version)

def start_script():
    system('title ' + script_title if name == 'nt' else 'PS1="\[\e]0;' + script_title + '\a\]"; echo $PS1')
    system('cls' if name == 'nt' else 'clear')
    print(f'''
    ..: {script_title} :..

    [!] ABOUT SCRIPT:
    [-] With this script, you can download wallpaper from site unsplash.com
    [-] Version: {script_version}
    --------
    [!] ABOUT CODER:
    [-] phnxXD, Programmer and developer from INDIA.
    [-] Website : phnxXD
    [-] Telegram : phnxXD
    --------
    ''')

def genString(stringLength):
    letters = ascii_letters + digits
    return ''.join(choice(letters) for i in range(stringLength))

def req(url):
    try:
        r = get(url)
    except:
        r = get(url)
    return r

def download():
    try:
        DOWNLOAD_FOLDER = download_folder.get()
        BASE_URL = 'https://source.unsplash.com'
        RES_URL = '1920x1080'
        num_images = int(num_images_entry.get())
        KEYWORDS = ['HD Wallpapers', 'Experimental', 'hope', 'travel', 'dark']
        Path(DOWNLOAD_FOLDER).mkdir(parents=True, exist_ok=True)
        for _ in range(num_images):
            FILE_NAME = 'unsplash-{}.jpg'.format(genString(7))
            FILE_PATH = '{}/{}'.format(DOWNLOAD_FOLDER, FILE_NAME)
            URL = '{}/{}/?{}'.format(BASE_URL, RES_URL, choice(KEYWORDS))
            img_data = req(URL).content
            with open(FILE_PATH, 'wb') as handler:
                handler.write(img_data)
        status_label.config(text="Wallpapers downloaded successfully!")
    except Exception as error:
        status_label.config(text="Error occurred: " + str(error))

def select_directory():
    folder_path = filedialog.askdirectory()
    download_folder.set(folder_path)

# Create the main window
root = tk.Tk()
root.title(script_title)

# Create and place widgets
start_script()

download_folder = tk.StringVar()

folder_label = tk.Label(root, text="Select Download Directory:")
folder_label.pack()

select_button = tk.Button(root, text="Select Directory", command=select_directory)
select_button.pack()

num_images_label = tk.Label(root, text="Number of Images to Generate:")
num_images_label.pack()

num_images_entry = tk.Entry(root)
num_images_entry.pack()

num_images_entry.insert(0, "10")  # Default value

download_button = tk.Button(root, text="Generate and Download", command=download)
download_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
