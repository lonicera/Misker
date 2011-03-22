#!/usr/bin/env python3
import os, subprocess, sys
def icon(line):
	line = int(line)
	if line == 0:
		olay = "-i /usr/share/icons/Faenza/status/48/audio-volume-muted-blocked-panel.png"
	elif line < 25:
		olay = "-i /usr/share/icons/Faenza/status/48/audio-volume-low.png"
	elif line < 75:
		olay = "-i /usr/share/icons/Faenza/status/48/audio-volume-medium-panel.png"
	elif line > 75:
		olay = "-i /usr/share/icons/Faenza/status/48/audio-volume-high.png"
	return olay



		

def goster(komut,ek):
	current_master = os.popen("amixer sget Master")
	old_prop = current_master.read()
	position = old_prop.find('%')
	line = old_prop[position-3:]
	line = line[:3]
	if not line.find('[') == "":
		pos = line.find('[')
		line = line[pos+1:]
	else:
		line = line
	if komut == "arttır":
		retri = "notify-send -u low -t 800 " + icon(line) + " 'Ses açiliyoru: %'"+line
	elif komut == "azalt":
		retri = "notify-send -u low -t 800 " + icon(line) + " 'Ses kısılıyoru: %'"+line
	elif komut == "kıs":
		retri = "notify-send -u low -t 800 " + icon(line) + " 'Sesi gapatıverdim gari'"
	elif komut == "ac":
		retri = "notify-send -u low -t 800 " + icon(line) + " 'Sesi açıverdim gari'"
	subprocess.Popen(retri, shell=True).wait()
	print(icon(line))


if sys.argv[1] == "arttır":
	command = "amixer set Master 5%+"
	subprocess.Popen(command, shell=True).wait()
	goster("arttır",0)
elif sys.argv[1] == "azalt": 
	command = "amixer set Master 5%-"
	subprocess.Popen(command, shell=True).wait()
	goster("azalt",0)
elif sys.argv[1] == "ackapa":

	current_master = os.popen("amixer sget Master")
	old_prop = current_master.read()
	position = old_prop.find('off')
	if position > 0:
		goster("ac",0)
	else:
		goster("kıs",0)
	command = "amixer set Master toggle"
	subprocess.Popen(command, shell=True).wait()

