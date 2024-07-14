#include <stdio.h>

int main()
{
	int size = 5;
	char array[5] = {};
	for(int i = 0; i < size; i++)
	{
		scanf(" %c", &array[i]);
	}

	for(int i = size - 1; i >= 0; i--)
	{
		printf("%c ", array[i]);
	}


	return 0;
}