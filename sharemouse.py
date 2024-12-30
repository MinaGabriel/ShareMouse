#!/usr/bin/env python
import sys
import time
import subprocess
import os
from mydaemon import Daemon

class ShareMouse(Daemon):
    def run(self):
        # Ensure that the plist file is copied to the correct location
        plist_file = '/Applications/ShareMouse/com.sharemouse.autoreload.plist'
        launch_agents_dir = os.path.expanduser('~/Library/LaunchAgents/')
        subprocess.call(f'sudo cp {plist_file} {launch_agents_dir}', shell=True)

        # Run the ShareMouse start/stop cycle every 5 minutes
        while True:
            self.sharemouseStop()
            self.sharemouseStart()
            time.sleep(300)

    def sharemouseStart(self):
        # Start ShareMouse application
        subprocess.call('open -a ShareMouse', shell=True)

    def sharemouseStop(self):
        # Stop ShareMouse application
        subprocess.call('killall ShareMouse', shell=True)

if __name__ == "__main__":
    daemon = ShareMouse('/tmp/sharemouse-process.pid')

    # Process command line arguments for daemon control
    if len(sys.argv) == 2:
        if sys.argv[1] == 'start':
            daemon.start()
        elif sys.argv[1] == 'stop':
            daemon.stop()
            daemon.sharemouseStop()
        elif sys.argv[1] == 'restart':
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print(f"Usage: {sys.argv[0]} start|stop|restart")
        sys.exit(2)
