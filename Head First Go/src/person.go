package main

import "fmt"

type Person struct {
	name   string
	age    int
	job    string
	salary int
}

func main() {
	var person_1 Person

	// Person specification
	person_1.name = "Dimas"
	person_1.age = 40
	person_1.job = "Software developer"
	person_1.salary = 250000

	// Access and print Person info
	fmt.Println("Name: ", person_1.name)
	fmt.Printf("The age of %s is: %d\n", person_1.name, person_1.age)
	fmt.Println("Job -> ", person_1.job)
	fmt.Println("Salary per year: ", person_1.salary)
}
