#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google Assistant GRPC recognizer."""

import argparse
import locale
import logging
import signal
import sys
import math
import time
import threading

from aiy.assistant.grpc import AssistantServiceClientWithLed
from aiy.board import Board
from aiy.leds import (Leds, Pattern, PrivacyLed, RgbLeds, Color)
from aiy.voice.audio import AudioFormat, play_wav, record_file, Recorder

def volume(string):
    value = int(string)
    if value < 0 or value > 100:
        raise argparse.ArgumentTypeError('Volume must be in [0...100] range.')
    return value

def locale_language():
    #language, _ = locale.getdefaultlocale()
    language, _ = locale.getdefaultlocale()
    return language

def main():
    logging.basicConfig(level=logging.DEBUG)
    signal.signal(signal.SIGTERM, lambda signum, frame: sys.exit(0))

    parser = argparse.ArgumentParser(description='Assistant service example.')
    parser.add_argument('--language', default=locale_language())
    parser.add_argument('--volume', type=volume, default=100)
    #args = parser.parse_args()

   # parser = argparse.ArgumentParser()
    parser.add_argument('--filename', '-f', default='recording.wav')
    args = parser.parse_args()
    talk = True

    with Board() as board:
        assistant = AssistantServiceClientWithLed(board=board,
                                                  volume_percentage=args.volume,
                                                  language_code=args.language)
        #done=threading.Event()
	
        while talk:#True:
          #  logging.info('Press button to start conversation...')
#            board.button.wait_for_press()
#            done = threading.Event()
#            board.button.when_pressed = done.set

            #def wait():
             #   start = time.monotonic()
              #  while not done.is_set():
               #     duration = time.monotonic() - start
                #    print('Recording: %.02f seconds [Press button to stop]' % duration)
                 #   time.sleep(0.5)

            #record_file(AudioFormat.CD, filename=args.filename, wait=wait, filetype='wav')

            
            #with Leds() as leds:
             #   leds.pattern = Pattern.blink(500)
              #  leds.update(Leds.rgb_pattern(Color.GREEN))
               # time.sleep(5)
            logging.info('Conversation started!')
            if not assistant.conversation2():
                board.button.wait_for_press()
                #play_wav(args.filename)
                #leds.update(Leds.rgb_pattern(Color.RED))
                #time.sleep(5)
            

if __name__ == '__main__':
    main()
