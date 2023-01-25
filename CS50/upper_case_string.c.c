#include <stdio.h>

int main()
{
    char buffer[50];
    printf("Give me a string, please: \n");
    fgets(buffer, 35, stdin);
    for (int i = 0; buffer[i]!='\0'; i++) {
    if(buffer[i] >= 'a' && buffer[i] <= 'z') {
       buffer[i] = buffer[i] -32;
          }
    }
    printf("Thank you for your string value! %s\n", buffer);
    return 0;
}
