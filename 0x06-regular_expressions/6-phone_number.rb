#!/usr/bin/env ruby
#the pattern should meet the 10 digit phone number
puts ARGV[0].scan(/\b[0-9]{10}\b/).join
