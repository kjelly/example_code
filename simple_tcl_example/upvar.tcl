proc fun2 {} {
    upvar 2 local_var my_var
    set my_var 10
}
proc fun1 { ctl } {
    upvar local_var my_var
    set my_var 8
    if { $ctl == 1} {
        fun2
    }
}

proc fun3 {} {
    uplevel { set local_var 15 } 

}

set local_var 5
puts $local_var
fun1 0
puts $local_var 
fun1 1
puts $local_var 
fun3
puts $local_var

