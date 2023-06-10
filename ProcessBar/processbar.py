import time

# https://github.com/Haj4li

a = '#'
b = ' '

def print_progress_bar(progress):
    bar_length = 50
    filled_length = int(round(bar_length * progress / 100))
    bar = a * filled_length + b * (bar_length - filled_length)
    percent = f'{progress}%'
    percent_pos = (bar_length - len(percent)) // 2
    bar = bar[:percent_pos] + percent + bar[percent_pos + len(percent):]
    print((f'[{bar}]'),end="\r")

for i in range(101):
    print_progress_bar(i)
    time.sleep(0.1)