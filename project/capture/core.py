from pathlib import Path 

from datetime import datetime, timezone 

import pyautogui 

import logging 

 

OUT = Path.cwd() / "out" 

OUT.mkdir(exist_ok=True) 

 

pyautogui.FAILSAFE = True 

pyautogui.PAUSE = 0.25 

 

##def ts() -> str: 

##    return datetime.now(timezone.utc).isoformat().replace("%Y-%m-%d_%H-%M-%S") 
def ts() -> str:
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
 

def take_screenshot(name: str) -> Path: 

    path = OUT / f"{name}_{ts()}.png" 

    img = pyautogui.screenshot() 

    img.save(path) 

    logging.info("Saved screenshot: %s", path) 

    return path 