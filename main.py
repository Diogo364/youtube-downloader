import os
import os.path as osp
from pytube import YouTube
from argparse import ArgumentParser

def download_from_url(url, outpath):
    try:
        video = YouTube(url)
        print(f'Downloading {video.title}')

        video_path = osp.join(outpath, f'{video.title}.mp4')

        stream = video.streams.get_highest_resolution()
        stream.download(filename=video_path)
        print('Downloaded')
    except Exception as e:
        print(f'An error ocurred: {e}')

if __name__ == '__main__':
    ap = ArgumentParser()
    ap.add_argument('-o', '--output', default='out', type=str, help='Specify the output directory for downloaded videos.')
    ap.add_argument('-i', '--input', type=str, default=None, help='Path to an input file containing a list of video URLs.')
    ap.add_argument('url', default=None, nargs='*', help='One or more video URLs to download. You can provide multiple URLs separated by spaces.')
    parser = ap.parse_args()

    assert any([parser.url, parser.input]), 'Please provide either an Input File, or a url.'

    os.makedirs(parser.output, exist_ok=True)

    if not parser.input is None:
        with open(parser.input, 'r') as in_file:
            url_list = in_file.read().split('\n')
    else:
        url_list = parser.url

    for url in url_list:
        download_from_url(url, parser.output)