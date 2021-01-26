package main

import "fmt"

func main() {
	var newPrice, oldPrice, qDif, growthPercentage float64

	println("Enter today's stock price on stock market:")
	fmt.Scan(&newPrice)

	println("Enter old stock price on stock market: ")
	fmt.Scan(&oldPrice)

	qDif = newPrice - oldPrice
	growthPercentage = (qDif / oldPrice) * 100
	var result = growthPercentage

	if result > 0 {
		fmt.Printf("The share price increased by: %3.3f percent\n", result)
	} else {
		fmt.Printf("The stock lost: %3.3f percentage in value\n", result)
	}

}
