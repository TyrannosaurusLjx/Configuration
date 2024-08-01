#!/bin/bash

# 初始化剪贴板内容
prev_clipboard=$(pbpaste)

# 无限循环来检测剪贴板内容变化
while true; do
  # 获取当前剪贴板内容
  current_clipboard=$(pbpaste)

  # 检查剪贴板内容是否变化
  if [ "$current_clipboard" != "$prev_clipboard" ]; then
    # 剪贴板内容发生变化，显示通知
    osascript -e "display notification \"$current_clipboard\" with title \"Clipboard Changed\""
    # 更新前一个剪贴板内容
    prev_clipboard="$current_clipboard"
  fi

  # 等待 1 秒后再检测
  sleep 1
done
