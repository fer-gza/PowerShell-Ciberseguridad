import subprocess
import pyautogui
import time
import logging
from datetime import datetime
from pathlib import Path

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3


def run_powershell(cmd: str):
    """
    Ejecuta un comando de PowerShell desde Python.
    Retorna una tupla con: (codigo_salida, salida, error)
    """
    try:
        result = subprocess.run(
            ["powershell", "-Command", cmd],
            capture_output=True, text=True, timeout=10
        )
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return 1, "", str(e)


def validate_data(data: dict) -> bool:
    """
    Valida que el diccionario 'data' contenga los campos requeridos.
    """
    required_fields = ["nombre", "correo", "equipo"]
    for field in required_fields:
        if field not in data or not data[field].strip():
            logging.error(f"Campo faltante o vacío: {field}")
            return False
    return True


def take_screenshot(name: str):
    """
    Captura una imagen de la pantalla con nombre y marca de tiempo UTC.
    Guarda las imágenes dentro del directorio 'out'.
    """
    out = Path("out")
    out.mkdir(exist_ok=True)
    ts = datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = out / f"{name}_{ts}.png"
    img = pyautogui.screenshot()
    img.save(path)
    logging.info(f"Captura guardada: {path}")
    return path


def fill_form(data: dict, start_coords: tuple[int, int]):
    """
    Automatiza el llenado del formulario web con PyAutoGUI.
    Las coordenadas deben establecerse manualmente.
    """
    logging.info(f"Iniciando llenado del formulario en {start_coords}")

    take_screenshot("before")
    pyautogui.click(start_coords)
    pyautogui.typewrite(data["nombre"])
    pyautogui.press("tab")
    pyautogui.typewrite(data["correo"])
    pyautogui.press("tab")
    pyautogui.typewrite(data["equipo"])
    pyautogui.press("enter")

    take_screenshot("during")
    time.sleep(1)
    take_screenshot("after")

    logging.info("Formulario completado correctamente.")