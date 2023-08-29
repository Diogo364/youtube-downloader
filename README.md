# YouTube Video Downloader

This Python script allows you to download YouTube videos using the Pytube library. You can provide either a list of video URLs directly as command-line arguments or specify an input file containing the URLs. The downloaded videos will be saved as MP4 files in the specified output directory.

## Prerequisites

- Python 3.x
- Pytube library

## Installation

1. Clone or download this repository to your local machine.
2. Navigate to the project directory.

```bash
cd youtube-downloader
```

3. Install the required dependencies using pip.

```bash
pip install pytube
```

## Usage

You can run the script from the command line using the following options:

```bash
python downloader.py [-h] [-o OUTPUT] [-i INPUT] [url [url ...]]
```

### Arguments

- `-h`, `--help`: Show a help message and exit.
- `-o OUTPUT`, `--output OUTPUT`: Specify the output directory for downloaded videos. Default is "out".
- `-i INPUT`, `--input INPUT`: Path to an input file containing a list of video URLs.
- `url [url ...]`: One or more video URLs to download. You can provide multiple URLs separated by spaces.

### Examples

1. Download videos by providing URLs directly:

```bash
python downloader.py -o downloads https://www.youtube.com/watch?v=video_url_1 https://www.youtube.com/watch?v=video_url_2
```

2. Download videos using an input file:

Create a text file named `urls.txt` and add video URLs on separate lines.

```
https://www.youtube.com/watch?v=video_url_1
https://www.youtube.com/watch?v=video_url_2
```

Run the script with the input file:

```bash
python downloader.py -i urls.txt -o downloads
```

## Output

Downloaded videos will be saved as MP4 files in the specified output directory.

## Disclaimer

Please use this script responsibly and respect YouTube's terms of service. Downloading copyrighted content without proper authorization may violate YouTube's policies and legal regulations.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to contribute to the project, report issues, or suggest improvements!
