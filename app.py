from pytube import YouTube
from pprint import pprint

# Link do video
yt = YouTube('https://www.youtube.com/watch?v=QYUXRpST1P0')

# Debugar opções de download disponíveis
streams = yt.streams
streamToList = lambda x: list(x) if x else '\nErro ao obter stream\n'
# pprint(streamToList(streams))

# Filtrando qual stream quero baixar
streams = streams.filter(progressive=True , mime_type='video/mp4', resolution="720p", )
print('\n\nStreams filtrados:')
pprint(streamToList(streams))

# Pegando primeiro da lista
stream = streams.first()
print('\n\nStreams escolhido: \n', stream)

# Faz download na pasta destino indicada
stream.download('./videos')