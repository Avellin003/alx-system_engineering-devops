#!/usr/bin/env ruby
#checks for capital letters in words and joins them
puts ARGV[0].scan(/[A-Z]/).join
