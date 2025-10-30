import os,glob
from exporters import *

def mp3_to_ogg(path):
	# Check if user provides a file path or directory path
	single_file = None
	if os.path.isfile(path):
		single_file = os.path.basename(path)
		path = os.path.dirname(path)

	os.chdir(path)
	if os.path.isdir('export'):
		pass
	else:
		os.mkdir('export')

	# Single file mode
	if single_file:
		name, ext = os.path.splitext(single_file)
		if ext != '.mp3':
			raise ValueError(f'File {single_file} is not an MP3 file')
		if os.path.isfile(f'export/{name}.ogg'):
			print(f"{name} is already exported as ogg file, skipping...")
		else:
			converter(name, ext, path, "ogg", "mp3")
	# Directory mode - batch convert all mp3 files
	else:
		if not glob.glob('*.mp3'): # Checking if the directory has mp3 files to convert
			raise FileNotFoundError(f'No MP3 files found on {path}')
		for i in os.listdir():
			if os.path.isdir(i):
				print("Skipping directories...")
			else:
				# Getting the name and extension name of the files in the specified path, then checking if their extension are .mp3
				# or if they are already .ogg, so we can skip it.
				# With that information, we can call the converter function
				name, ext = os.path.splitext(i)
				if os.path.isfile(f'export/{name}.ogg') or ext == ".ogg":
					print(f"{name} is already exported as ogg file, skipping...")
				elif ext !='.mp3':
					print("Skipping not mp3 files...")
				else:
					converter(name,ext,path,"ogg","mp3")

def ogg_to_mp3(path):
	# Check if user provides a file path or directory path
	single_file = None
	if os.path.isfile(path):
		single_file = os.path.basename(path)
		path = os.path.dirname(path)

	os.chdir(path)
	if os.path.isdir('export'):
		pass
	else:
		os.mkdir('export')

	# Single file mode
	if single_file:
		name, ext = os.path.splitext(single_file)
		if ext != '.ogg':
			raise ValueError(f'File {single_file} is not an OGG file')
		if os.path.isfile(f'export/{name}.mp3'):
			print(f"{name} is already exported as mp3 file, skipping...")
		else:
			converter(name, ext, path, "mp3", "ogg")
	# Directory mode - batch convert all ogg files
	else:
		if not glob.glob('*.ogg'):
			raise FileNotFoundError(f'No ogg files found on {path}')
		for i in os.listdir():
			if os.path.isdir(i):
				print("Skipping directories...")
			else:
				name, ext = os.path.splitext(i)
				if os.path.isfile(f'export/{name}.mp3') or ext == ".mp3":
					print(f'{name} is already exported as mp3 file, skipping...')
				elif ext !='.ogg':
					print("Skipping not ogg files...")
				else:
					converter(name,ext,path,"mp3","ogg")

		    	
def main():
	"""Main entry point for the audio converter CLI."""
	try:
		while True:
			print('===============')
			print('Audio converter')
			print('===============')
			print('[1] Mp3 to Ogg')
			print('[2] Ogg to Mp3')
			print('[3] Exit')
			print('===============')
			op = int(input('Select an option -> '))
			print('===============')
			if op==1:
				print("Write the path where the mp3 files are for export them as ogg")
				path = input('MP3 Path -> ')
				mp3_to_ogg(path)
			elif op==2:
				print("Write the path where the ogg files are for export them as mp3")
				path = input('OGG Path -> ')
				ogg_to_mp3(path)
			elif op==3:
				break


	except FileNotFoundError as NoFilesFound:
		print(NoFilesFound)
	except ValueError as e:
		print(f"Error: {e}")
	except KeyboardInterrupt:
		print("\nProgram interrupted by user.")
	else:
		print("Program finalized succesfully")

	finally:
		print("Program finalized.")

if __name__ == '__main__':
	main()

		
		
