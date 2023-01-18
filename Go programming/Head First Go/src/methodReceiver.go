//package main
//
//import "fmt"
//
//type Contact struct {
//	name string
//	age  int
//}
//
//func main() {
//	x := Contact{"Frank", 45}
//	x.welcome()
//}
//
//func (x Contact) welcome() {
//	fmt.Println(x.name)
//	fmt.Println(x.age)
//}

/* the same functionality as the regular function  that takes a struct as its argument */

package main

import "fmt"

type Contact struct {
	name string
	age  int
}

func welcome(x Contact) {
	fmt.Println(x.name)
	fmt.Println(x.age)
}
func main() {
	x := Contact{"James", 42}
	welcome(x)
}
