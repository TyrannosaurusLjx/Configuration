tell application "iTerm"
    tell current window
        create tab with default profile
        tell current session of current tab
            write text "cd ~ && FZF_DEFAULT_COMMAND='find . -path ./Library -prune -o -type f -print' fzf | xargs open"
        end tell
    end tell
    activate
end tell
