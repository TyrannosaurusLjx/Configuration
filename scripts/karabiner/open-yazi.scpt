tell application "iTerm"
    tell current window
        create tab with default profile
        tell current session of current tab
            write text "cd ~/Desktop && yazi"
        end tell
    end tell
    activate
end tell
