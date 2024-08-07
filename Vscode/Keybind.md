# keybind

```json
// 将键绑定放在此文件中以覆盖默认值
[
    //文件树配置
    {
        "key": "cmd+e",
        "command": "workbench.files.action.focusFilesExplorer",
        "when": "editorTextFocus && explorerViewletVisible && neovim.mode != insert"
    },
    {
        "key": "cmd+e",
        "command": "workbench.action.closeSidebar",
        "when": "explorerViewletVisible && filesExplorerFocus && neovim.mode != insert"
    },
    {
        "key": "cmd+e",
        "command": "workbench.view.explorer",
        "when": "!explorerViewletVisible && neovim.mode != insert"
    },
    {
        "key": "escape",
        "command": "workbench.action.focusActiveEditorGroup",
        "when": "explorerViewletVisible && filesExplorerFocus && neovim.mode != insert"
    },
    //导航, leader+hjkl 移动
    {
        "key" : "space shift+h",
        "command": "workbench.action.moveEditorToPreviousGroup",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    {
        "key" : "space shift+l",
        "command": "workbench.action.moveEditorToNextGroup",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    {
        "key" : "space shift+j",
        "command": "workbench.action.moveEditorToBelowGroup",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    {
        "key" : "space shift+k",
        "command": "workbench.action.moveEditorToAboveGroup",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    {
        "key": "space h",
        "command": "workbench.action.navigateLeft",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    {
        "key": "space j",
        "command": "workbench.action.navigateDown",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    {
        "key": "space k",
        "command": "workbench.action.navigateUp",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    {
        "key": "space l",
        "command": "workbench.action.navigateRight",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    //normal 移动
    {
        "key": "cmd+j",
        "command": "cursorDown",
        "when": "neovim.mode == insert && editorTextFocus"
    },
    {
        "key": "cmd+k",
        "command": "cursorUp",
        "when": "neovim.mode == insert && editorTextFocus"
    },
    {
        "key": "cmd+h",
        "command": "cursorLeft",
        "when": "neovim.mode == insert && editorTextFocus"
    },
    {
        "key": "cmd+l",
        "command": "cursorRight",
        "when": "neovim.mode == insert && editorTextFocus"
    },
    {
        "key": "cmd+j",
        "command": "runCommands",
        "when": "neovim.mode == normal",
        "args": {
            "commands": [
                "cursorDown",
                "cursorDown",
                "cursorDown",
            ]
        }
    },
    {
        "key": "cmd+k",
        "command": "runCommands",
        "when": "neovim.mode == normal",
        "args": {
            "commands": [
                "cursorUp",
                "cursorUp",
                "cursorUp",
            ]
        }
    },
    {
        "key": "cmd+h",
        "command": "runCommands",
        "when": "neovim.mode == normal",
        "args": {
            "commands": [
                "cursorLeft",
                "cursorLeft",
                "cursorLeft",
            ]
        }
    },
    {
        "key": "cmd+l",
        "command": "runCommands",
        "when": "neovim.mode == normal",
        "args": {
            "commands": [
                "cursorRight",
                "cursorRight",
                "cursorRight",
            ]
        }
    },
    {
        "key": "shift+j",
        "command": "cursorPageDown",
        "when": "neovim.mode == normal"
    },
    {
        "key": "shift+k",
        "command": "cursorPageUp",
        "when": "neovim.mode == normal"
    },
    //tab 管理
    {
        "key": "cmd+1",
        "command": "workbench.action.openEditorAtIndex1",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    {
        "key": "cmd+2",
        "command": "workbench.action.openEditorAtIndex2",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    {
        "key": "cmd+3",
        "command": "workbench.action.openEditorAtIndex3",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    {
        "key": "cmd+4",
        "command": "workbench.action.openEditorAtIndex4",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    {
        "key": "cmd+5",
        "command": "workbench.action.openEditorAtIndex5",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    {
        "key": "cmd+6",
        "command": "workbench.action.openEditorAtIndex6",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    {
        "key": "cmd+7",
        "command": "workbench.action.openEditorAtIndex7",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    {
        "key": "cmd+8",
        "command": "workbench.action.openEditorAtIndex8",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    {
        "key": "cmd+9",
        "command": "workbench.action.openEditorAtIndex9",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    {
        "key": "cmd+0",
        "command": "workbench.action.lastEditorInGroup",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    {
        "key": "cmd+[",
        "command": "workbench.action.previousEditor",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    {
        "key": "cmd+]",
        "command": "workbench.action.nextEditor",
        "when": "editorTextFocus && neovim.mode != insert"
    },
    //搜索
    {
        "key": "cmd+shift+e",
        "command": "workbench.action.showAllEditors",
        "when": "neovim.mode != insert"
    },
    {
        "key": "cmd+shift+f",
        "command": "workbench.action.replaceInFiles",
        "when": "neovim.mode != insert"
    },
    //最近打开的文件
    {
        "key": "cmd+r",
        "command": "workbench.action.openRecent",
        "when": "neovim.mode != insert"
    },
    //最近的项目
    {
        "key": "cmd+shift+r",
        "command": "workbench.action.openRecent",
        "when": "neovim.mode != insert"
    },
    //保存并回到 normal
    {
        "key": "cmd+s",
        "command": "runCommands",
        "when": "neovim.mode == insert",
        "args": {
            "commands": [
                "workbench.action.files.save",
                "vscode-neovim.escape"
            ]
        }
    },
    // cmd+shift+p 和 ; 一样
    {
        "key": ";",
        "command": "workbench.action.showCommands",
        "when": "neovim.mode == 'normal'"
    },
    // 单独设置编辑页面字体大小
    {
        "key": "cmd+=",
        "command": "editor.action.fontZoomIn",
        "when": "editorTextFocus"
    },
    {
        "key": "cmd+-",
        "command": "editor.action.fontZoomOut",
        "when": "editorTextFocus"
    },
    {
        "key": "cmd+0",
        "command": "editor.action.fontZoomReset",
        "when": "editorTextFocus"
    },
    //补全
    {
        "key": "cmd+l",
        "command": "editor.action.inlineSuggest.acceptNextWord",
        "when": "neovim.mode == insert && inlineSuggestionVisible && !editorReadonly"
    },
    {
        "key": "tab",
        "command": "selectNextSuggestion",
        "when": "editorTextFocus && suggestWidgetMultipleSuggestions && suggestWidgetVisible"
    },
    {
        "key": "shift+tab",
        "command": "selectPrevSuggestion",
        "when": "editorTextFocus && suggestWidgetMultipleSuggestions && suggestWidgetVisible"
    },
    //删除
    {
        "key": "cmd+backspace",
        "command": "deleteRight",
        "when": "editorTextFocus && neovim.mode == 'insert'"
    },
    //设置  F8
//    {
//     "key": "F8",
//     "command": "markdown-preview-enhanced.openPreviewToTheSide",
//     "when": "editorFocus && neovim.mode == 'normal' && resourceExtname == .md"
//    },

   //bookmark set
   {
    "key": "space b m",
    "command": "bookmarks.toggle",
    "when": "editorTextFocus && neovim.mode == 'normal'"
    },
    {
        "key": "space b n",
        "command": "bookmarks.jumpToNext",
        "when": "editorTextFocus && neovim.mode == 'normal'"
    },
    {
        "key": "space b p",
        "command": "bookmarks.jumpToPrevious",
        "when": "editorTextFocus && neovim.mode == 'normal'"
    },
    {
        "key": "space b c",
        "command": "bookmarks.clear",
        "when": "editorTextFocus && neovim.mode == 'normal'"
    },
    {
        "key": "space b l",
        "command": "bookmarks.list",
        "when": "editorTextFocus && neovim.mode == 'normal'"
    },

    // code runner
    {
        "key": "F8",
        "command": "markdown-preview-enhanced.openPreviewToTheSide",
        "when": "editorFocus && neovim.mode == 'normal' && resourceExtname == .md"
    },
    {
        "key": "F8",
        "command": "code-runner.runByLanguage",
        "when": "resourceExtname != .md"
    }

]
```
