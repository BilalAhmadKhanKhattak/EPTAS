import os
import colorama
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from colorama import Fore

colorama.init(autoreset=True)

banner = """
_______ ______ _______ _______  ______ 
(_______|_____ (_______|_______)/ _____)
 _____   _____) )  _    _______( (____  
|  ___) |  ____/  | |  |  ___  |\____ \ 
| |_____| |       | |  | |   | |_____) )
|_______)_|       |_|  |_|   |_(______/     v 1.0

"EVERY PICTURE TELLS A STORY"
This Tool Extracts The Metadata From An Image
Currently Supported formats .jpg .png etc.


Created BY B.A.K AKA MR. BILRED After A MENTAL BREAKDOWN
This Way, I Converted My Stress/Anxiety into Productivity!
Programming, My Coping Mechanism ;)
                         
"""
print(Fore.LIGHTMAGENTA_EX + banner)

def extract_exif(file_path):
    try:
        img = Image.open(file_path)  # opens the image using "Image.open" method from PIL
        exif_data = img.getexif() or {}  # for some images "_getexif" works

        if not exif_data:
            print("Sorry, I couldn't find any metadata...")

        metadata = {}
        for tag_id, value in exif_data.items():  # Each key is a TAG ID, Each Value is metadata value
            tag_name = TAGS.get(tag_id, tag_id)  # Use TAG ID if no readable name exists
            metadata[tag_name] = value

        if "GPSInfo" in metadata:
            gps_info = metadata["GPSInfo"]
            gps_data = {}

            for gps_id, gps_value in gps_info.items():
                gps_tag = GPSTAGS.get(gps_id, gps_id)
                gps_data[gps_tag] = gps_value
            metadata["GPSInfo"] = gps_data

        return metadata

    except Exception as e:
        return {"error": str(e)}


def display_metadata(metadata):
    if "error" in metadata:
        print(f"Error:  {metadata['error']}")
        return
    for tag, value in metadata.items():
        print(Fore.LIGHTMAGENTA_EX + f"{tag}: {value}")

    # for me, I guess, what I'm doing isn't some "course" or "destination", It's a journey
    # maybe, a never ending journey...
    

if __name__ == "__main__":
    file_path = input(Fore.LIGHTCYAN_EX + "Enter The Path to your image: ")
    if os.path.exists(file_path):
        metadata = extract_exif(file_path)
        display_metadata(metadata)

    else:
        print("FIle not found")

    input("Enter any key to exit...")

    #  I Know, Everything Will Be Alright, InshaAllah!
