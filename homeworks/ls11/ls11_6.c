#include <stdio.h>
#include <string.h>

int main()
{
	char array[] = "hello";
	int count = 0;
	for(int i = 0; array[i] != '\0'; i++)
	{
		count++;
	}
	printf("%d\n", count );
	return 0;
}