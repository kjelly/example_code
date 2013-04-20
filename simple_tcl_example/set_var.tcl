#! /bin/env tcl
# the default argument of c is 5.
proc test {a b {c 5}} {
    set ret [expr "$a + $b + $c"]
    puts $ret
    return $ret
}

proc test_global {} {
    set ::a 5
}

set a a
puts $a
set b $a
puts $b
set b {$a}
puts $b
set b "$a"
puts $b
set b [expr "1 + 1"]
puts $b

set ::a 1
puts $::a

test_global
puts $::a

test 1 2 3
test 1 2
