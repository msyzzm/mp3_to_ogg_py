import time
from time import sleep
from pydub import AudioSegment
from progress.spinner import PixelSpinner

def converter(name,ext,path,form,type):
	with PixelSpinner(f'{name} Processing... ') as bar:
		for i in range(100):
			sleep(0.03)
			bar.next()
		if type=="ogg":
			sound = AudioSegment.from_ogg(name+ext)
			sound.export(f"{path}/export/{name}.{form}", format=form)
		elif type=="mp3":
			sound = AudioSegment.from_mp3(name+ext)
			sound.export(f"{path}/export/{name}.{form}", format=form)
		
