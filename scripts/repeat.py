#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title repeat
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "Placeholder" }
# @raycast.needsConfirmation true

# Documentation:
# @raycast.description repeat send msg
# @raycast.author junxun_luo
# @raycast.authorURL https://raycast.com/junxun_luo

import sys
import subprocess
import keyboard

msg = sys.argv[1]

# 重复输入 msg 并回车 
def main():
    for _ in range(2):
        keyboard.press_and_release('esc')
        keyboard.write(msg)
        subprocess.run(['osascript', '-e', 'tell application "System Events" to keystroke return'])
    
if __name__ == '__main__':
    main()










