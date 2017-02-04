import os

DIR = "audio"
FORMAT = "mp3"

def play(basename):
    filename = "%s/%s.%s" % (DIR, str(basename), FORMAT)
    cmd = "mpg321 %s" % filename
    os.system(cmd)

def test():
    play("pleaseRun")
    play("10")
    play("50")
    play("100")
    play("clickTakatsuka")
    play("done")
    play("nice")
    play("goodjob")
    play("notClick")
    
if __name__ == "__main__":
    test()
