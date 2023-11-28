#!/usr/bin/env python3
import os
import re
import glob
#import time

def clear_console():
    if os.name == "posix":  # for Unix
        os.system("clear")
    else:  # for windows
        os.system("cls")

def shift_subtitle_time(subtitle, shift):
    start_t, end_t = subtitle.group(1), subtitle.group(2)
    shifted_start_t = shift_time(start_t, shift)
    shifted_end_t = shift_time(end_t, shift)
    return f"{shifted_start_t} --> {shifted_end_t}"

def shift_time(time_str, shift):
    hours, minutes, secs, msecs = re.split(r"[:,]", time_str)
    total_msecs = int(hours)*3600000 + int(minutes)*60000 + int(secs)*1000 + int(msecs)
    shifted_msecs = total_msecs + shift
    shifted_hours, remainder = divmod(shifted_msecs, 3600000)
    shifted_minutes, remainder = divmod(remainder, 60000)
    shifted_secs, shifted_msecs = divmod(remainder, 1000)
    return f"{pad_zero(shifted_hours)}:{pad_zero(shifted_minutes)}:{pad_zero(shifted_secs)},{pad_zero(shifted_msecs, 3)}"

def pad_zero(value, length=2):
    return str(value).zfill(length)

def file_edit(input_path, output_path, time_shift):
    with open(input_path, "r") as input_file, open(output_path, "w") as output_file:
        for line in input_file:
            match = re.match(r"(\d+:\d+:\d+,\d+) --> (\d+:\d+:\d+,\d+)", line)
            if match:
                shifted_time_line = shift_subtitle_time(match, time_shift)
                output_file.write(shifted_time_line + "\n")
            else:
                output_file.write(line)

def main():
    time_shift = int(float( input("Enter the shift time (+ Forward, - Backward): ").replace(",", ".") )*1000)
    folder_path = input("Enter the folder path: ")
    file_names = input("Enter file names separated by commas: ")
    file_names_list = [name.strip() for name in file_names.split(",")]          # The strip() method is used to remove any leading or trailing spaces from each file name also can indicate the
                                                                                # character to remove: txt = ",,,rrttgg....EXAMPLE....rrr" 
    for file_name in file_names_list:                             # x = txt.strip(",.grt")
        search_pattern = os.path.join(folder_path, f"{file_name}.srt") # It can be use a ".*" to search for a coincidence with every file extension  
        input_path = search_pattern
        output_path = os.path.join(folder_path, f"{file_name}_shifted.srt")
        #input_path = str(glob.glob(search_pattern)).strip("[]''")
        #print(f"{input_path} Tipo: {type(input_path)}")
        file_edit(input_path, output_path, time_shift)

if __name__ == "__main__":
    #start_time = time.time() #Used to record the execution time
    main()
    #end_time = time.time()
    #execution_time = end_time - start_time
    #print(f"Execution time: {execution_time}")

    # C:\Users\Felipe\Downloads\ThW.S01
    # S01E01, S01E02, S01E03, S01E04, S01E05, S01E06, S01E07, S01E08, S01E09, S01E10, S01E11, S01E12, S01E13