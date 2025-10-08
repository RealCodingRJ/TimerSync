import asyncio
import time
from typing import TypeAlias

TimerTyped: TypeAlias = int

def get_time():
    return time.sleep(1)

async def get_Timer() -> None:
    timer = TimerTyped(1)
    running = True

    try:
        while running:
            timer += 1


            if timer == 25 * 60:
                print("[Timer] DONE")
            else:
                get_time()
                print("[Seconds]", timer)

    except NameError:
        print("Error")

asyncio.run(get_Timer())