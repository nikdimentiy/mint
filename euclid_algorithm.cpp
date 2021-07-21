#include <iostream>
using namespace std;

int main()
{
    int64_t a;
    int64_t b;


    cout << "Enter two integer number separated by space: " << endl;
    cin >> a >> b;
    while (a != 0 and b != 0) {
        if (a > b) {
            cout << "DEBUG : Case 1 -> " << a << " : " << b << endl;
            a = a % b;
        } else {
            cout << "DEBUG : Case 2 -> " << a << " : " << b << endl;
            b = b % a;
        }
    }
    cout << "The greatest common divisor is: ";
    cout << (a + b) << endl;
}