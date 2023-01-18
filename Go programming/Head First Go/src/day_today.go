package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("What day today?")
	today := time.Now().Weekday()
	switch today {
	case 1:
		fmt.Println("Monday")
	case 2:
		fmt.Println("Tuesday")
	case 3:
		fmt.Println("Wednesday")
	case 4:
		fmt.Println("Thursday")
	case 5:
		fmt.Println("Friday")
	case 6:
		fmt.Println("Saturday")
	case 7:
		fmt.Println("Sunday")
	default:
		fmt.Println("I don't know how to handle this!'")
	}
}
