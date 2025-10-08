import asyncio
import time
from string import Template
from typing import TypeAlias

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
                print("[Timer] DONE")

                if timer == 60:
                    print("1 Minute Past")

                elif timer == 60 * 2:
                    print("2 Minutes Past")

                elif timer == 60 * 3:
                    print("3 Minutes Past")

                elif timer == 60 * 4:
                    print("4 Minutes Past")

                elif timer == 60 * 5:
                    print("5 Minutes Past")

                elif timer == 60 * 6:
                    print("6 Minutes Past")

                elif timer == 60 * 7:
                    print("7 Minutes Past")

                elif timer == 60 * 8:
                    print("8 Minutes Past")

                elif timer == 60 * 9:
                    print("9 Minutes Past")

                elif timer == 60 * 10:
                    print("10 Minutes Past")

                elif timer == 60 * 11:
                    print("11 Minutes Past")

                elif timer == 60 * 12:
                    print("12 Minutes Past")

                elif timer == 60 * 13:
                    print("13 Minutes Past")

                elif timer == 60 * 14:
                    print("14 Minutes Past")

                elif timer == 60 * 15:
                    print("15 Minutes Past")

                elif timer == 60 * 16:
                    print("16 Minutes Past")

                elif timer == 60 * 17:
                    print("17 Minutes Past")

                elif timer == 60 * 18:
                    print("18 Minutes Past")

                elif timer == 60 * 19:
                    print("19 Minutes Past")

                elif timer == 60 * 20:
                    print("20 Minutes Past")

                elif timer == 60 * 21:
                    print("21 Minutes Past")

                elif timer == 60 * 22:
                    print("22 Minutes Past")

                elif timer == 60 * 23:
                    print("23 Minutes Past")

                elif timer == 60 * 24:
                    print("24 Minutes Past")

                elif timer == 60 * 25:
                    print("Timer Done")

            else:
                get_time()
                print("[Seconds]", TIMESeconds.substitute(seconds=timer))

    except NameError:
        print("Error")

asyncio.run(get_Timer())