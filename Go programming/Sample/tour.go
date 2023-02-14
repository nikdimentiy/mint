// package main

// import "fmt"

// func split(sum int) (y, x int) {
// 	x = sum * 3 / 2
// 	y = sum - x
// 	return
// }

// func main() {
// 	fmt.Println(split(5))
// }

// package main

// import "fmt"

// var c, python, java bool

// func main() {
// 	var i int
// 	fmt.Println(i, c, python, java)
// }

package main

import (
	"fmt"
	"reflect"
)

var i, j = 1, 2.7

func main() {
	var c, python, java = true, false, "no!"
	fmt.Println(reflect.TypeOf(j))
	fmt.Println(i, j, c, python, java)
}
