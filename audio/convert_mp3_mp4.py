from moviepy.editor import *

def mp3_to_mp4(audio_path, image_path, output_path):
    audio = AudioFileClip(audio_path)
    image = ImageClip(image_path, duration=audio.duration)
    image.fps = 24  # Add this line

    video = image.set_audio(audio)
    video.write_videofile(output_path, codec='libx264')

mp3_to_mp4('StardewValleyLecture.mp3', 'image.png', 'Stardew_Audio.mp4')