import subprocess

def TrimAudio(audio):

    chemin_ffmpeg = r"C:\Users\NOAH DERAND\Documents\FFMPEG\ffmpeg-8.0-full_build\bin\ffmpeg.exe"
    chemin_audio = audio
    chemin_sortie = r"output\test.mp3"

    # Couper les 5 premières secondes
    subprocess.run([
        chemin_ffmpeg,
        "-y",  # overwrite
        "-i", chemin_audio,
        "-ss", "1.67",  # durée en secondes
        chemin_sortie
    ])
    return chemin_sortie