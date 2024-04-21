import os.path as osp
from enum import Enum
from pytube import YouTube, Playlist

class DownloadTypes(Enum):
    VIDEO='.mp4'
    AUDIO='.mp3'

    def serialize(self):
        return {'type': self.name, 'extension': self.value}

class YoutubeDownloader:
    def __init__(self, url=None, stream_type=DownloadTypes.VIDEO, playlist=False):
        self.url = url
        self.videos = None
        self.curr_video = None
        self.stream = None
        self.stream_type = stream_type
        self.playlist = playlist
    
    @staticmethod
    def parse_media_options(media: DownloadTypes):
        return media.serialize()
    
    @property
    def stream_type(self):
        return self.__stream_type
    
    @stream_type.setter
    def stream_type(self, value):
        self.__stream_type = self.parse_media_options(value)
    
    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    def parse_filename_from_current_video(self, extension='.mp4'):
        return f'{self.curr_video.title}{extension}'

    def set_output_path(self, out_root, extension):
        return osp.join(out_root, self.parse_filename_from_current_video(extension))
    
    def set_current_video(self, video):
        self.curr_video = video

    def set_video(self):
        self.videos = Playlist(self.url).videos if self.playlist else [YouTube(self.url)]

    def get_current_video_stream(self):
        self.stream = self.curr_video.streams.get_highest_resolution()
    
    def get_current_audio_stream(self):
        self.stream = self.curr_video.streams.get_audio_only()
        
    def download(self, out_root: str):
        self.set_video()
        for video in self.videos:
            try:
                self.set_current_video(video)
                print(f'Downloading {self.curr_video.title}')
                
                out_path = self.set_output_path(out_root, self.stream_type['extension'])
                if self.stream_type['type'] == 'VIDEO':
                    self.get_current_video_stream()
                elif self.stream_type['type'] == 'AUDIO':
                    self.get_current_audio_stream()
                else:
                    raise Exception(f"No implementation for {self.stream_type['type']}")
                
                self.stream.download(filename=out_path)
                print('Downloaded')
            except Exception as e:
                print(f'An error ocurred: {e}')