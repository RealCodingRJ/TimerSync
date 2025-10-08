from typing import TypeAlias

TIME: TypeAlias = int

def timerSettingConverted(time: TIME, message: str):
    print(f"Current Time: {time} [SECONDS]: {message}")