#!/usr/bin/env bash
import os

def main():
    clear_console()
    change = 0.0
    ntime = "00:31:58,184 --> 00:32:01,449"
    while True:
        change = float(input("Enter the amount of time to change: "))
        if change != 0:
            break
        else:
            print("Enter a valid number")

    for total_secs in time_to_secs(ntime):
        print(secs_to_time(total_secs + change))

    print("\t---END---")

def time_to_secs(time):
#   time = time.replace(",",".")
#	time_split = time.split(":")
#	hours = time_split[0]; minutes = time_split[1]; secs = time_split[2]
#	hours = float(hours); minutes = float(minutes); secs = float(secs)
    time_line = time.replace(",", ".").split(" --> ") #Replace , for . and split the text before and after the -->
    total_secs = 0.0
    for x in time_line:
        hours, minutes, secs = map(float, x.split(":"))
        total_secs = hours*3600 + minutes*60 + secs
        yield total_secs

def secs_to_time(total_secs):
    hours = int(total_secs/3600)
    total_secs %= 3600
    minutes = int(total_secs/60)
    secs = round(total_secs%60, 3) # Round the result to 3 decimal points
    time_line = f"{hours:02d}:{minutes:02d}:{secs}".replace(".", ",")
    return time_line    

def clear_console():
    if os.name == "posix":  # for Unix
        os.system("clear")
    else:  # for windows
        os.system("cls")

if __name__=="__main__":
	main ()