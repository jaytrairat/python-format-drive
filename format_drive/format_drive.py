import argparse
import subprocess
import urllib.request

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--drive", required=True, help="Drive location to be formatted")
    parser.add_argument("-v", "--volume_name", required=True, help="New volume name for the drive after formatting")
    args = parser.parse_args()

    confirm = input(f"Are you sure you want to format {args.drive} to exFAT with volume name {args.volume_name} (yes/no)? ")
    if confirm.lower() != "yes":
        return

    try:
        subprocess.run(["format", args.drive, "/FS:exFAT", "/V:" + args.volume_name, "/Q"], check=True)
    except subprocess.CalledProcessError as error:
        print(f"Error while formatting the drive: {error}")
        return

    icon_url = "https://raw.githubusercontent.com/jaytrairat/icons/main/jaytrairat-trimmy.ico"
    icon_path = args.drive + "autorun.inf"
    try:
        urllib.request.urlretrieve(icon_url, icon_path)
    except urllib.error.URLError as error:
        print(f"Error while downloading the icon: {error}")
        return

    print(f"Drive {args.drive} has been successfully formatted to exFAT with volume name {args.volume_name} and autorun.inf icon")

if __name__ == "__main__":
    main()
