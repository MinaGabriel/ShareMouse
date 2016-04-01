#!/usr/bin/env python
import sys, time, subprocess
from daemon import Daemon

class ShareMouse(Daemon):
        def run(self):

                subprocess.call(' sudo cp /Applications/ShareMouse/com.sharemouse.autoreload.plist ~/Library/LaunchAgents/', shell=True)
                while True:
                        self.sharemouseStop()
                        self.sharemouseStart()
                        time.sleep(300)
        def sharemouseStart(self):
              subprocess.call('open -a ShareMouse', shell=True)
        def sharemouseStop(self):
             subprocess.call('killall ShareMouse', shell=True)

if __name__ == "__main__":
        daemon = ShareMouse('/tmp/daemon-example.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                        daemon.sharemouseStop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)
