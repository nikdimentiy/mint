/**
 * @file stack_trace_example.c
 * @brief Demonstrates a simple function call stack.
 * 
 * This program showcases a series of function calls, illustrating how 
 * the call stack operates in a typical C program. It consists of three 
 * functions: `A`, `B`, and `C`, which call each other in a nested manner. 
 * The `main` function initiates the call sequence, and each function 
 * prints messages to indicate when it is called and when it returns.
 * 
 * - `main()` calls `A()`.
 * - `A()` calls `B()`.
 * - `B()` calls `C()`.
 * 
 * The sequence of print statements reflects the order of function calls
 * and returns, demonstrating how the stack grows and shrinks.
 * 
 * Example Output:
 * main() called.
 *   A() called.
 *     B() called.
 *       C() called.
 *       C() returns.
 *     B() returns.
 *   A() returns.
 * main() returns.
 */

#include <stdio.h>

// Function prototypes
void A();
void B();
void C();

/**
 * @brief Entry point of the program.
 * 
 * Prints a message indicating that `main()` is called. Calls function `A()`,
 * and then prints a message indicating that `main()` is returning. 
 * 
 * @param argc Number of command-line arguments.
 * @param argv Array of command-line argument strings.
 * @return int Exit status of the program.
 */
int main(int argc, char* argv[])
{
    printf("main() called.\n");
    A();  // Calls function A
    printf("main() returns.\n");

    return 0;  // Exit the program
}

/**
 * @brief Function A.
 * 
 * Prints a message indicating that `A()` is called. Calls function `B()`,
 * and then prints a message indicating that `A()` is returning.
 */
void A()
{
    printf("  A() called.\n");
    B();  // Calls function B
    printf("  A() returns.\n");
}

/**
 * @brief Function B.
 * 
 * Prints a message indicating that `B()` is called. Calls function `C()`,
 * and then prints a message indicating that `B()` is returning.
 */
void B()
{
    printf("    B() called.\n");
    C();  // Calls function C
    printf("    B() returns.\n");
}

/**
 * @brief Function C.
 * 
 * Prints a message indicating that `C()` is called, followed by a message 
 * indicating that `C()` is returning.
 */
void C()
{
    printf("      C() called.\n");
    printf("      C() returns.\n");
}
