#!/bin/bash

# 获取剪贴板内容
clip_content=$(pbpaste)

# 转义剪贴板内容中的双引号
escaped_clip_content=$(printf '%s' "$clip_content" | sed 's/"/\\"/g')

# 使用 osascript 显示通知
osascript -e "display notification \"$escaped_clip_content\" with title \"Copied\""
