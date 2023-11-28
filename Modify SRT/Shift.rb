def shift_subtitle_time(subtitle, shift)
    start_time, end_time = subtitle[1], subtitle[2]
    shifted_start_time = shift_time(start_time, shift)
    shifted_end_time = shift_time(end_time, shift)
    "#{shifted_start_time} --> #{shifted_end_time}"
end

def shift_time(time_str, shift)
    hours, minutes, seconds, milliseconds = time_str.split(/[:,]/)
    total_milliseconds = hours.to_i*3600000 + minutes.to_i*60000 + seconds.to_i*1000 + milliseconds.to_i
    shifted_milliseconds = total_milliseconds + shift
    shifted_hours, remainder = shifted_milliseconds.divmod(3600000)
    shifted_minutes, remainder = remainder.divmod(60000)
    shifted_seconds, shifted_milliseconds = remainder.divmod(1000)
    "#{pad_zero(shifted_hours)}:#{pad_zero(shifted_minutes)}:#{pad_zero(shifted_seconds)},#{pad_zero(shifted_milliseconds, 3)}"
end

def pad_zero(value, length = 2)
    value.to_s.rjust(length, '0')
end

def main
    # Example usage
    input_file_path = "S01E01.srt"
    output_file_path = "S01E01_shifted.srt"
    time_shift = 2000  # Shift the subtitles 2 seconds forward

    File.open(input_file_path, 'r') do |input_file|
        File.open(output_file_path, 'w') do |output_file|
            input_file.each_line do |line|
                match = line.match(/(\d+:\d+:\d+,\d+) --> (\d+:\d+:\d+,\d+)/)
                if match
                    shifted_time_line = shift_subtitle_time(match, time_shift)
                    output_file.puts shifted_time_line
                else
                output_file.puts line
                end
            end
        end
    end
end

def clear_console
    if RUBY_PLATFORM =~ /linux|darwin/  # for Unix-like systems (Linux, macOS)
      system "clear"
    else  # for Windows
      system "cls"
    end
end

#start_time = Time.now #Used to record the execution time
main
#end_time = Time.now
#execution_time = end_time - start_time
#puts "Execution time: #{execution_time}"