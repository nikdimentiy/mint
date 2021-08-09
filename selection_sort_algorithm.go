package main

import "fmt"

func main() {
	array := [9]int{2, 1, 4, 3, 5, 9, 7, 6, 8}

	for i := 1; i < len(array); i++ {
		temp := array[i]
		j := i

		for ; j > 0 && array[j-1] >= temp; j-- {
			array[j] = array[j-1]
		}
		array[j] = temp
	}

	for sortedVal := range array {
		fmt.Println(sortedVal)
	}
}
