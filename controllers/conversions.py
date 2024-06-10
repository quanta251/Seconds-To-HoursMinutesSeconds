import numpy as np


def seconds2hours(seconds: int) -> list[int]:
    minutes: int = int(np.fix(seconds / 60))
    hours: int = int(np.fix(minutes / 60))
    remaining_seconds: int = seconds - (minutes * 60)
    remaining_minutes: int = minutes - (hours * 60)
    return [hours, remaining_minutes, remaining_seconds]


def main():
    mytime: int = 25478685

    time_list: list[int] = seconds2hours(mytime)
    print(f'''
    Hours: {time_list[0]}
    Minutes: {time_list[1]}
    Seconds: {time_list[2]}''')


if __name__ == "__main__":
    main()
