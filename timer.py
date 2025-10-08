import asyncio
import time
from string import Template
from typing import TypeAlias
from TimerSecondsConverted import timerSettingConverted

TimerTyped: TypeAlias = int

def get_time():
    return time.sleep(1)

TIMESeconds: Template = Template("$seconds")

async def get_Timer() -> None:
    timer = TimerTyped(1)
    running = True

    try:
        while running:
            timer += 1

            if timer == 25 * 60:

                timerSettingConverted(timer, "1 Minute Past")

            elif timer == 60 * 2:
                timerSettingConverted(timer, "2 Minutes Past")

            elif timer == 60 * 3:
                timerSettingConverted(timer, "3 Minutes Past")


            elif timer == 60 * 4:
                timerSettingConverted(timer, "3 Minutes Past")


            elif timer == 60 * 5:
                timerSettingConverted(timer, "5 Minutes Past")


            elif timer == 60 * 6:
                timerSettingConverted(timer, "6 Minutes Past")


            elif timer == 60 * 7:
                timerSettingConverted(timer, "7 Minutes Past")


            elif timer == 60 * 8:
                timerSettingConverted(timer, "8 Minutes Past")

            elif timer == 60 * 9:
                timerSettingConverted(timer, "9 Minutes Past")

            elif timer == 60 * 10:
                timerSettingConverted(timer, "10 Minutes Past")

            elif timer == 60 * 11:

                timerSettingConverted(timer, "11 Minutes Past")

            elif timer == 60 * 12:
                timerSettingConverted(timer, "12 Minutes Past")

            elif timer == 60 * 13:
                timerSettingConverted(timer, "13 Minutes Past")

            elif timer == 60 * 14:
                timerSettingConverted(timer, "14 Minutes Past")

            elif timer == 60 * 15:
                timerSettingConverted(timer, "15 Minutes Past")

            elif timer == 60 * 16:
                timerSettingConverted(timer, "16 Minutes Past")

            elif timer == 60 * 17:
                timerSettingConverted(timer, "17 Minutes Past")

            elif timer == 60 * 18:
                timerSettingConverted(timer, "18 Minutes Past")

            elif timer == 60 * 19:
                timerSettingConverted(timer, "19 Minutes Past")

            elif timer == 60 * 20:
                timerSettingConverted(timer, "20 Minutes Past")

            elif timer == 60 * 21:
                timerSettingConverted(timer, "21 Minutes Past")

            elif timer == 60 * 22:
                timerSettingConverted(timer, "22 Minutes Past")

            elif timer == 60 * 23:
                timerSettingConverted(timer, "23 Minutes Past")

            elif timer == 60 * 24:
                timerSettingConverted(timer, "24 Minutes Past")

            elif timer == 60 * 25:
                timerSettingConverted(timer, "Done")
            else:
                get_time()

    except NameError:
        print("Error")

asyncio.run(get_Timer())