from pathlib import Path
from string import ascii_letters, digits
from random import choice
from time import sleep
from requests import get

script_version = '1.0'
script_title = 'Unsplash WP Downloader by ALIILAPRO (version {})'.format(script_version)

def start_script():
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

def download(num_images):
    try:
        download_folder = Path("wp")
        if not download_folder.exists():
            download_folder.mkdir(parents=True, exist_ok=True)
        BASE_URL = 'https://source.unsplash.com'
        RES_URL = '1920x1080'
        num_images = int(num_images)
        KEYWORDS = ['HD Wallpapers', 'Experimental', 'hope', 'travel', 'dark']
        for _ in range(num_images):
            FILE_NAME = 'unsplash-{}.jpg'.format(genString(7))
            FILE_PATH = download_folder / FILE_NAME
            URL = '{}/{}/?{}'.format(BASE_URL, RES_URL, choice(KEYWORDS))
            img_data = req(URL).content
            with open(FILE_PATH, 'wb') as handler:
                handler.write(img_data)
        print("Wallpapers downloaded successfully!")
    except Exception as error:
        print("Error occurred:", error)

def run_without_gui():
    start_script()
    num_images = input("Enter the number of images to generate: ")
    download(num_images)

run_without_gui()
