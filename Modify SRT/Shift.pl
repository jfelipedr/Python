#!/usr/bin/env perl
use strict;
#Use warnings;
#Use Term::ANSIColor;
use Time::HiRes qw(gettimeofday); #Used to record the execution time

sub shift_subtitle_time 
{
    my ($subtitle, $shift) = @_;
    my ($start_time, $end_time) = ($subtitle =~ /(\d+:\d+:\d+,\d+) --> (\d+:\d+:\d+,\d+)/);
    my $shifted_start_time = shift_time($start_time, $shift);
    my $shifted_end_time = shift_time($end_time, $shift);
    return "$shifted_start_time --> $shifted_end_time";
}

sub shift_time 
{
    my ($time_str, $shift) = @_;
    my ($hours, $minutes, $seconds, $milliseconds) = ($time_str =~ /(\d+):(\d+):(\d+),(\d+)/);
    my $total_milliseconds = $hours*3600000 + $minutes*60000 + $seconds*1000 + $milliseconds;
    my $shifted_milliseconds = $total_milliseconds + $shift;
    my ($shifted_hours, $remainder) = divmod($shifted_milliseconds, 3600000);
    my ($shifted_minutes, $remainder) = divmod($remainder, 60000);
    my ($shifted_seconds, $shifted_milliseconds) = divmod($remainder, 1000);
    return sprintf("%02d:%02d:%02d,%03d", $shifted_hours, $shifted_minutes, $shifted_seconds, $shifted_milliseconds);
}

sub divmod 
{
    my ($dividend, $divisor) = @_;
    my $quotient = int($dividend / $divisor);
    my $remainder = $dividend % $divisor;
    return ($quotient, $remainder);
}

sub main 
{
    #clear_console();
    # Example usage
    my $input_file_path = "S01E01.srt";
    my $output_file_path = "S01E01_shifted.srt";
    my $time_shift = 2000;  # Shift the subtitles 2 seconds forward

    open(my $input_file, '<', $input_file_path) or die "Cannot open input file: $!";
    open(my $output_file, '>', $output_file_path) or die "Cannot open output file: $!";

    while (my $line = <$input_file>) 
    {
        if (my ($start_time, $end_time) = ($line =~ /(\d+:\d+:\d+,\d+) --> (\d+:\d+:\d+,\d+)/)) {
            my $shifted_time_line = shift_subtitle_time($line, $time_shift);
            print $output_file $shifted_time_line . "\n";
        } else {
            print $output_file $line;
        }
    }
    close($input_file);
    close($output_file);
}

sub clear_console 
{
    if ($^O =~ /linux|darwin/) {  # for Unix-like systems (Linux, macOS)
        system "clear";
    } else {  # for Windows
        system "cls";
    }
}

#my $start_time = gettimeofday();
main();
#my $end_time = gettimeofday();
#my $execution_time = $end_time - $start_time;
#print "Execution time: $execution_time \n";