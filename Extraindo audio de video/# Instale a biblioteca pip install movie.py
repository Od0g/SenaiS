# Instale a biblioteca pip install moviepy
#Importe a biblioteca 

from moviepy.video.io.VideoFileClip import VideoFileclip

# Função para extrair o audio de um video
def extrair_audio(video_path, audio_path):

    video = VideoFileclip(video_path ) #Carregar o video

    audio = video.audio #Extração do audio do video

    audio.write_audiofile(audio_path) # Salvar o audio
    video.close()# Fechar o video

#exemplo de vso
    
video_path = "video.mp4" #caminho do video que será extraido

audio_path = "audio.mp3" #caminho do audio que será salvo

extrair_audio(video_path, audio_path)# extrair o audio do video e salvar