// first positional literal in number
package main

import (
	"fmt"
	"strconv"
)

func main() {
	var number int
	fmt.Scan(&number)

	s := strconv.Itoa(number)
	fmt.Println(s[0:1])
}
