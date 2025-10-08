import asyncio
import time
from string import Template
from typing import TypeAlias

from TimerSecondsConverted import timerSettingConverted

TimerTyped: TypeAlias = int

def get_time():
    return time.sleep(1)

TIMESeconds: Template = Template("$seconds")


async def get_Timer():
    timer = 1

    while True:
        timer += 1
        get_time()

        if timer == 60 * 1:
            timerSettingConverted("1 Minute Past")

        if timer == 60 * 2:
            timerSettingConverted("2 Minutes Past")

        if timer == 60 * 3:
            timerSettingConverted("3 Minutes Past")

        if timer == 60 * 4:
            timerSettingConverted("3 Minutes Past")

        if timer == 60 * 5:
            timerSettingConverted("5 Minutes Past")

        if timer == 60 * 6:
            timerSettingConverted("6 Minutes Past")

        if timer == 60 * 7:
            timerSettingConverted("7 Minutes Past")

        if timer == 60 * 8:
            timerSettingConverted("8 Minutes Past")

        if timer == 60 * 9:
            timerSettingConverted("9 Minutes Past")

        if timer == 60 * 10:
            timerSettingConverted("10 Minutes Past")

        if timer == 60 * 11:
            timerSettingConverted("11 Minutes Past")

        if timer == 60 * 12:
            timerSettingConverted("12 Minutes Past")

        if timer == 60 * 13:
            timerSettingConverted("13 Minutes Past")

        if timer == 60 * 14:
            timerSettingConverted("14 Minutes Past")

        if timer == 60 * 15:
            timerSettingConverted("15 Minutes Past")

        if timer == 60 * 16:
            timerSettingConverted("16 Minutes Past")

        if timer == 60 * 17:
            timerSettingConverted("17 Minutes Past")

        if timer == 60 * 18:
            timerSettingConverted("18 Minutes Past")

        if timer == 60 * 19:
            timerSettingConverted("19 Minutes Past")

        if timer == 60 * 20:
            timerSettingConverted("20 Minutes Past")

        if timer == 60 * 21:
            timerSettingConverted("21 Minutes Past")

        if timer == 60 * 22:
            timerSettingConverted("22 Minutes Past")

        if timer == 60 * 23:
            timerSettingConverted("23 Minutes Past")

        if timer == 60 * 24:
            timerSettingConverted("24 Minutes Past")

        if timer == 60 * 25:
            timerSettingConverted("Done")

        else:
            print("Seconds: ", timer)

asyncio.run(get_Timer())