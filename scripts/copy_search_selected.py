# pyperclip,pyautogui
import pyperclip, pyautogui
import subprocess
# 模拟键盘按键复制选中文本
pyautogui.hotkey('command', 'c', interval=0.05)
# 复制剪贴板内容
copied_text = pyperclip.paste()

search_engines = {  
    "zhihu": "https://www.zhihu.com/search?type=content&q=",  
    "bilibili": "https://search.bilibili.com/all?keyword=",  
    "blibli": "https://search.bilibili.com/all?keyword=",  
    "cc98": "https://www.cc98.org/search?boardId=0&keyword=",  
    "github": "https://github.com/search?q=",  
    "bing": "https://cn.bing.com/search?q=",  
    "google": "https://www.google.com.hk/search?q=",  
    "douying": "https://www.douyin.com/search/"  
}  

def has_engine(copied_text):
    if ":" in copied_text:
        engine, query = copied_text.split(":")
        if engine in search_engines:
            return engine, query
    return None, copied_text
  
def search(query, engine):  
    if engine in search_engines:  
        search_url = str(search_engines[engine] + query)  
    else:  
        search_url = str(search_engines["bing"]+query)  
    subprocess.run(["open", search_url], check=True)    

def main():
    engine, query = has_engine(copied_text)
    if engine:
        search(query, engine)
    else:
        search(copied_text, "bing")

if __name__ == "__main__":
    main()