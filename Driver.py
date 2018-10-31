from MarkovBuilder import MarkovBuilder
from m2pconverter import MIDI2PIXConverter
from p2mconverter import PIX2MIDIConverter
import os
import sys
from random import shuffle

from os import listdir
from os.path import isfile, join
targetDir = './starwars/'
songs = [targetDir + f for f in listdir(targetDir) if isfile(join(targetDir, f)) and f.endswith('.mxl')]
print(len(songs))
maxSongs = 15
order = 10
shuffle(songs)

# songs = ['spider.mxl', 'mega.mxl']

songPNGs = []
for song in songs[:maxSongs]:
    try:
        songPNGs.append(MIDI2PIXConverter(song, debug=True).buildImage())
    except:
        pass

markovName = 'storewors'
markovOutFile = markovName + str(order) + 'Out.png'
outMidiFile = markovName + str(order) + 'Out.mid'
# inputFile = 'spider.mxl'
# outFile = os.path.splitext(inputFile)[0] + '.png'
# markovOutFile = 'markov' + outFile
# outMidiFile = 'markov' + os.path.splitext(inputFile)[0] + '.mid'

MarkovBuilder(songPNGs, order=order).generateRandomSong(markovOutFile, songLength=300)
PIX2MIDIConverter(markovOutFile).buildMidi(outMidiFile)