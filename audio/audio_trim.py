from pydub import AudioSegment
import os

filepath = "video_2_audio.mp3"

# Load the MP3 file
audio = AudioSegment.from_file(filepath, format="mp3")

# Check the size of the MP3 file in bytes
size = os.path.getsize(filepath)

# If the size of the MP3 file is already below 10MB, you can stop here. Otherwise, calculate the duration of the file in milliseconds
if size < 10 * 1024 * 1024:
    print("File size is already below 10MB.")
else:
    duration = len(audio)
    target_bitrate = (9 * 1024 * 1024 * 8) / duration
    audio.export("video_2_trimmed.mp3", format="mp3", bitrate=f"{target_bitrate}k")
    print("New MP3 file created successfully.")

