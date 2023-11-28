#!/usr/bin/env ruby
#checks for patterns that start with the h and ends with n
puts ARGV[0].scan(/^h.{1}n$/).join
