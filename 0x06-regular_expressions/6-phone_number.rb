#!/usr/bin/env ruby
#the pattern should meet the 10 digit phone number
puts ARGV[0].scan(/d.{1,10}).join
