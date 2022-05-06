package main

import "fmt"

type deck []string

func (my_deck deck) print() {
	for index, card := range my_deck {
		fmt.Println(index, card)
	}
}
