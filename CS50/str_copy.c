#include <stdio.h>

int main()
{
	char str_1[] = "programming is ";
	char str_2[] = "awesome";

	int length, j;

	length = 0;
	while (str_1[length] != '\0')
	{
		length++;
	}

	for (j = 0; str_2[j] != '\0'; j++, length++)
	{
		str_1[length] = str_2[j];
	}

	str_1[length] = '\0';
	printf("After concatenation --> the string is: %s\n", str_1);
	return 0;
}
