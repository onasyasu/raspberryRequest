#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, time, urllib
import play_audio as audio

# for import dash_sensor
sys.path.append('../git/dash-sensor')
import step

# A or B
ME="B"
YOU="A"

DICT_USERNAME = {
    "A": "Kawasaki",
    "B": "Hashimoto"
}

BASE_URL = "http://state-api.au-syd.mybluemix.net/state"

def run():
    
    ### dash_sensor
    print "dash_sensor"
    time.sleep(1)
    audio.play("10")
    time.sleep(1)
    audio.play("20")
    time.sleep(1)
    audio.play("30")
    print "dash done."
    ### dash_sensor
    
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
                os.system("curl http://state-api.au-syd.mybluemix.net/state/")
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
