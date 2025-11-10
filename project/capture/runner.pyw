import subprocess, time, logging 

from pathlib import Path 

from core import take_screenshot 

 

LOG = Path.cwd() / "run.log" 

logging.basicConfig(filename=str(LOG), level=logging.INFO, 

                    format="%(asctime)s %(levelname)s %(message)s", encoding="utf-8") 

 

def launch_calculator(): 

    return subprocess.Popen(["calc.exe"])  # Asume Windows 

 

def main(): 

    logging.info("Start flow") 

    take_screenshot("before_open") 

    proc = launch_calculator() 

    time.sleep(1.2) 

    take_screenshot("with_app") 

    try: 

        proc.terminate() 

        proc.wait(timeout=3) 

    except Exception: 

        try: 

            proc.kill() 

        except Exception: 

            pass 

    time.sleep(0.6) 

    take_screenshot("after_close") 

    logging.info("End flow") 

    print("Done: screenshots in out/ and log run.log") 

 

if __name__ == "__main__": 

    main() 