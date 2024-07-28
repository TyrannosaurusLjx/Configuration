#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title ranger
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖

# Documentation:
# @raycast.description open ranger with iterm
# @raycast.author junxun_luo
# @raycast.authorURL https://raycast.com/junxun_luo

open -a iTerm "`which ranger`"
