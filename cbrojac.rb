#!/usr/bin/env ruby

ukupno_karaktera = 0
ukupno_redova = 0
datoteke = Dir.glob("**/*.py")

if datoteke.empty?
  puts " Нису пронађене .py датотеке у директоријуму"
  exit
end

puts " Статистика по датотеци:"
puts "-" * 50

datoteke.each do |datoteka|
  sadrzaj = File.read(datoteka)
  broj_karaktera = sadrzaj.length
  broj_redova = sadrzaj.split(/\r\n|\r|\n/).length
  
  ukupno_karaktera += broj_karaktera
  ukupno_redova += broj_redova
  
  puts " #{datoteka}:"
  puts "   Карактера: #{broj_karaktera}"
  puts "   Редова: #{broj_redova}"
  puts
end

puts "-" * 50
puts " Укупна статистика:"
puts "   Укупно (.py) датотека: #{datoteke.count}"
puts "   Укупно карактера: #{ukupno_karaktera}"
puts "   Укупно редова: #{ukupno_redova}"
puts "-" * 50