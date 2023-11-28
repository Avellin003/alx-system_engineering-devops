#!/usr/bin/env ruby
#checks for the proper writing of both the sender
#and the receiver phone numbers and the proper usage of flags
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).jion(",") 
