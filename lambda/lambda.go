package main

import (
    "fmt"
)

func map_func(array []int, fun func(int)int){
    for index, element := range array{
        array[index] = fun(element)
    }
}
func main(){
    v := []int{1, 2 ,3 ,4 , 5}
    fmt.Println(v)
    map_func(v, func(s int)int{return s * s})
    fmt.Println(v)
}
