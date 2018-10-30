from MarkovBuilder import MarkovBuilder
from m2pconverter import MIDI2PIXConverter
from p2mconverter import PIX2MIDIConverter
import os
import sys

inputFile = 'spider.mxl'
outFile = os.path.splitext(inputFile)[0] + '.png'
markovOutFile = 'markov' + outFile
outMidiFile = 'markov' + os.path.splitext(inputFile)[0] + '.mid'

MIDI2PIXConverter(inputFile).buildImage()
MarkovBuilder(outFile).generateRandomSong(markovOutFile, songLength=200)
PIX2MIDIConverter(markovOutFile).buildMidi(outMidiFile)