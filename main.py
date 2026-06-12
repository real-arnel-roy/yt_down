import yt_dlp


def progress_hooks(d):
    print(d["_percent_str"])

    if d["status"] == "finished":
        print("Finished!!!")


ydl_opts = {"outtmpl": "download/%(title)s.%(ext)s", "progress_hooks": [progress_hooks]}


def download_vid(url):
    try:
        print("downloading......")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:  # type: ignore
            ydl.download([url])

        print("Downloaded")
    except Exception as e:
        print("Download Failed!!!")
        print(f"Error: {e}")


def get_info(url):
    try:
        with yt_dlp.YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=False)

        title = info.get("title", "Unknown")
        uploader = info.get("uploader", "Unknown")
        durat = info.get("duration", 0)
        views = info.get("view_count", "Unknown")
        upload_date = info.get("upload_date", "Unknown")
        formats = len(info.get("formats", []))  # type: ignore

        minutes = durat // 60  # type: ignore
        seconds = durat % 60  # type: ignore

        print("\n========== VIDEO INFO ==========")
        print(f"Title       : {title}")
        print(f"Uploader    : {uploader}")
        print(f"Duration    : {minutes}m {seconds}s")
        print(f"Views       : {views}")
        print(f"Upload Date : {upload_date}")
        print(f"Formats     : {formats}")
        print("================================")

    except Exception as e:
        print(f"Error: {e}")


url = input("Enter YouTube URL: ")
while True:
    print("---Menu---")
    print("1. Get Info \n2. Download\n3. EXIT")
    print("----------")
    ch = int(input("\n\nWhat do you Choose - "))

    if ch == 1:
        get_info(url)

    elif ch == 2:
        download_vid(url)
    elif ch == 3:
        break
    else:
        print("Invalid Option")
