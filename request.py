#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, time, urllib
import play_audio as audio

# for import step in dash_sensor
sys.path.append('../git/dash-sensor')
import step

########## SETTINGS ##########
ME = "B"
YOU = "A"
MAX_STEP_COUNT = 100
DICT_USERNAME = {
    "A": "Kawasaki",
    "B": "Hashimoto"
}
##############################

BASE_URL = "http://state-api.au-syd.mybluemix.net/state"

def run():
    total_step_count = 0
    print "dash_sensor"
    while total_step_count < MAX_STEP_COUNT:
        step.count()
        total_step_count += 10
        print total_step_count
        audio.play(str(total_step_count))
    print "dash done."
    
    url = "%s/endRun%s" % (BASE_URL, ME)
    try:
        result = urllib.urlopen( url ).read().strip()
    except ValueError:
        print "アクセスに失敗しました。"
        
    audio.play("done")
    audio.play("nice")
    audio.play("goodjob")
    
    wait()

    
def wait():
    isSoundable = None
    url = "%s/getSoundableUser%s" % (BASE_URL, ME)
    while True:
        try:
            isSoundable = urllib.urlopen( url ).read().strip()
            if   isSoundable == "true":
                audio.play("click%s" % DICT_USERNAME[YOU])
                audio.play("pleaseRun")
                break
            elif isSoundable == "false":
                pass
            print url, isSoundable
        except ValueError:
            print "アクセスに失敗しました。"
        time.sleep(1)
        
    run()

    
def main():
    wait()
    
if __name__ == "__main__":
    main()
