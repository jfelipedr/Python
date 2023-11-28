import os, re, glob

def clear_console():
    if os.name == "posix":  # for Unix
        os.system("clear")
    else:  # for windows
        os.system("cls")

def file_edit(input_path, output_path, time_shift):
    print(f"Files edited from: '{input_path}', and saved in '{output_path}', shifted {time_shift} seconds 😀")

def main():
    clear_console()
    #time_shift = int(float( input("Enter the shift time (+ Forward, - Backward): ").replace(",", ".") )*1000)
    folder_path = input("Enter the folder path: ")
    file_names = input("Enter file names separated by commas: ")
    file_names_list = [name.strip() for name in file_names.split(",")]          # The strip() method is used to remove any leading or trailing spaces from each file name also can indicate the
    files = [" "]*len(file_names_list)                                         # character to remove: txt = ",,,rrttgg....EXAMPLE....rrr" 
    for i, file_name in enumerate(file_names_list):                                           # x = txt.strip(",.grt")
        search_pattern = os.path.join(folder_path, f"{file_name}.srt") # It can be use a ".*" to search for a coincidence with every file extension
        print(glob.glob(search_pattern)) # The extend() method is used to add the matching file paths for each file name to the files list.   
        files[i] = glob.glob(search_pattern)
    
    print(files)
    #output_path = "S01E01_shifted.srt"
    #file_edit(input_path, output_path, time_shift)

main()
# C:\Users\Felipe\Downloads\ThW.S01
# S01E01, S01E02, S01E03, S01E04, S01E05, asdas