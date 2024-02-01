# 将文本转为语音
from gtts import gTTS


tts = gTTS('刘德华德华德华德华德华德华德华德华德华德华德华', lang="zh-CN")
tts.save('hello.mp3')
