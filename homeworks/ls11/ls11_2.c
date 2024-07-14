#include <stdio.h>

int main()
{
	int array[] = {1, 2, 3, 4, 5};
	int size = sizeof(array) / sizeof(int);

	int* ptr = array;
	for(int i = 0; i < size; i++)
	{
		printf("%d\n", *(ptr + i));
	}
	return 0;
}