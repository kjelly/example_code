#! /bin/env tcl

gets stdin input
if { $input < 5 } {
    puts "your input, $input < 5"
} else {
    puts "your input, $input >= 5"
}

set counter 5

while { $counter > 0 } {
    puts $counter
    incr counter -1
}

for {set counter 0} { $counter < 10 } { incr counter 1 } {
    if { $counter > 5 } {
        break
    } elseif { $counter % 2 == 0} {
        continue
    } else {
        puts $counter
    }
}
