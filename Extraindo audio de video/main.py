# Instale a biblioteca pip install moviepy
#Importe a biblioteca 

from moviepy.video.io.VideoFileClip import VideoFileClip

# Função para extrair o audio de um video
def extrair_audio(video_path, audio_path):

    video = VideoFileClip(video_path ) #Carregar o video

    audio = video.audio #Extração do audio do video

    audio.write_audiofile(audio_path) # Salvar o audio
    video.close()# Fechar o video

#exemplo de vso
    
video_path = "STHPRKT07EP08.mp4" #caminho do video que será extraido

audio_path = "STHPRKT07EP08.mp3" #caminho do audio que será salvo

extrair_audio(video_path, audio_path)# extrair o audio do video e salvar