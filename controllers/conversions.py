import numpy as np


def seconds2hours(seconds: int) -> list[int]:
    minutes: int = int(np.fix(seconds / 60))
    hours: int = int(np.fix(minutes / 60))
    remaining_seconds: int = seconds - (minutes * 60)
    remaining_minutes: int = minutes - (hours * 60)
    return [hours, remaining_minutes, remaining_seconds]


def seconds2days(seconds: int) -> list[int]:
    minutes: int = int(np.fix(seconds / 60))
    hours: int = int(np.fix(minutes / 60))
    days: int = int(np.fix(hours / 24))
    remaining_seconds: int = seconds - (minutes * 60)
    remaining_minutes: int = minutes - (hours * 60)
    remaining_hours: int = hours - (days * 24)
    return [days, remaining_hours, remaining_minutes, remaining_seconds]


def main():
    mytime: int = 25478685

    time_list: list[int] = seconds2hours(mytime)
    days_list: list[int] = seconds2days(mytime)
    print(f'''
    Hours: {time_list[0]}
    Minutes: {time_list[1]}
    Seconds: {time_list[2]}''')
    print("==========================")
    print(f'''
    Days: {days_list[0]}
    Hours: {days_list[1]}
    Minutes: {days_list[2]}
    Seconds: {days_list[3]}
    ''')


if __name__ == "__main__":
    main()
