package main
import (
    "fmt"
    "time"
)

func out(from, to int) {
  for i:=from; i<=to; i++ {
    time.Sleep(50 * time.Millisecond)
    fmt.Println(i)
  }
}
func main() {
  out(0, 5)
  out(6, 10)
}
