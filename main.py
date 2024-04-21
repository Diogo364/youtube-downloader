import os
from argparse import ArgumentParser
from models import DownloadTypes, YoutubeDownloader

if __name__ == '__main__':
    ap = ArgumentParser()
    ap.add_argument('-o', '--output', default='out', type=str, help='Specify the output directory for downloaded videos.')
    ap.add_argument('-i', '--input', type=str, default=None, help='Path to an input file containing a list of video URLs.')
    ap.add_argument('--audio', action='store_true', default=False, help='Download only audio from video (mp3).')
    ap.add_argument('--url', default=None, nargs='*', help='One or more video URLs to download. You can provide multiple URLs separated by spaces.')
    ap.add_argument('--playlist', action='store_true', help='Flag to treat URL as a Playlist to download entire content.')
    parser = ap.parse_args()
    print(parser)

    assert any([parser.url, parser.input]), 'Please provide either an Input File, or a url.'

    os.makedirs(parser.output, exist_ok=True)

    stream_type = DownloadTypes.AUDIO if parser.audio else DownloadTypes.VIDEO

    yd = YoutubeDownloader(stream_type=stream_type, playlist=parser.playlist)

    if not parser.input is None:
        with open(parser.input, 'r') as in_file:
            url_list = in_file.read().split('\n')
    else:
        url_list = parser.url

    for url in url_list:
        yd.url = url
        yd.download(parser.output)