#!/usr/bin/env python3
import os
import re #module to work with regular expressions
#import time #Use to record the time

def main():
    # Example usage
    input_file_path = "S01E01.srt" #Path of the original file to modify
    output_file_path = "S01E01_shifted.srt" #Path of the output file
    time_shift = 2000  # Shift the subtitles 2 seconds forward

    with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file: #open origin file on read mode and the output on write mode
        for line in input_file:
            match = re.match(r"(\d+:\d+:\d+,\d+) --> (\d+:\d+:\d+,\d+)", line) #checks the string to be matched for a pattern, so that "\d+" match the hours,
            if match:                                                          #minutes, secs, or msecs.
                shifted_time_line = shift_subtitle_time(match, time_shift)
                output_file.write(shifted_time_line + "\n")
            else:
                output_file.write(line)

def shift_subtitle_time(subtitle, shift):
    start_time, end_time = subtitle.group(1), subtitle.group(2)     # The match group is for example:
    shifted_start_time = shift_time(start_time, shift)              #match.group(0) or match.group(): "00:00:01,000 --> 00:00:02,500"
    shifted_end_time = shift_time(end_time, shift)                  #match.group(1): "00:00:01,000" (start time)
    return f"{shifted_start_time} --> {shifted_end_time}"           #match.group(2): "00:00:02,500" (end time)

def shift_time(time_str, shift):
    hours, minutes, seconds, milliseconds = re.split(r"[:,]", time_str) #Splits the start and end time between each ":" and ","
    total_milliseconds = int(hours)*3600000 + int(minutes)*60000 + int(seconds)*1000 + int(milliseconds)
    shifted_milliseconds = total_milliseconds + shift
    shifted_hours, remainder = divmod(shifted_milliseconds, 3600000) #The divmod() method returns their quotient and remainder in a tuple. (quotient, remainder) like a division %
    shifted_minutes, remainder = divmod(remainder, 60000)
    shifted_seconds, shifted_milliseconds = divmod(remainder, 1000)
    return f"{pad_zero(shifted_hours)}:{pad_zero(shifted_minutes)}:{pad_zero(shifted_seconds)},{pad_zero(shifted_milliseconds, 3)}"

def pad_zero(value, length=2):
    return str(value).zfill(length) #fill the string with zeros until it is "2" by default (or the "length" value) charaters long

def clear_console():
    if os.name == "posix":  # for Unix systems
        os.system("clear")
    else:  # for windows
        os.system("cls")

if __name__=="__main__":
    #start_time = time.time() 
    main ()
    #end_time = time.time()
    #execution_time = end_time - start_time #Used to record the execution time
    #print(f"Execution time: {execution_time}")