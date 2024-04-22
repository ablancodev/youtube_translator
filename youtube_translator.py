import os
import pytube

''' OpenAI api_key '''
openai_api_key = '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'

''' get a param from python console '''
import sys
print(sys.argv[1])

''' si viene un parametro, es el id del video '''
if len(sys.argv) > 1:
  youtubeUrl = "https://www.youtube.com/watch?v=" + sys.argv[1]
else:
  youtubeUrl = "https://www.youtube.com/watch?v=ZQ3_sq7K3w0"


youtubeVideo = pytube.YouTube(youtubeUrl)

audio = youtubeVideo.streams.filter(only_audio=True).first()
audio.download(filename='videoyou_aldi.mp4')


from pathlib import Path
from openai import OpenAI

''' audio to text '''
client = OpenAI(api_key = openai_api_key)

speech_file_path = "video_audio.mp4"
audio_file = open(speech_file_path, "rb")
response = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text"
)

print(response)

''' chatgpt translate this text '''
response = client.chat.completions.create(
  model="gpt-4",
  messages=[
	{"role": "system", "content": "You are a helpful spanish translator. Not verbose, only give me the tanslation.Please translate this text to spanish:"},
	{"role": "user", "content": response}
  ]
)

print(response.choices[0].message.content)

''' texto to audio '''
client = OpenAI(api_key = openai_api_key)

speech_file_path = "video_auto_translated.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=response.choices[0].message.content[:3800]
)

response.stream_to_file(speech_file_path)
