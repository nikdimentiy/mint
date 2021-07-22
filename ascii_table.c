// The program show: uppercase and lowercase letter in ASCII table
// American Standard Code for Information Interchange, is a character encoding 
// standard for electronic communication. ASCII codes represent text in computers, 
// telecommunications equipment, and other devices. Most modern character-encoding 
// schemes are based on ASCII, although they support many additional characters

#include <stdio.h>

int main(void)

{
	for (int i = 65; i < 65 + 26; i++)
	{
		printf("%c: %i\n", (char) i, i);
	}


	printf("\n");


	for (int i = 97; i < 97 + 26; i++)
	{
		printf("%c: %i\n", (char) i, i);
	}
	
	return 0;
}
