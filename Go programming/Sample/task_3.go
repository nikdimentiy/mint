package main

import "fmt"

func main() {
	var x, p, y, years int
	fmt.Scan(&x, &y, &y)

	for ; x < y; years++ {
		x += x * p / 100
	}
	fmt.Println(years)
}
