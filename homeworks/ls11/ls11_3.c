#include <stdio.h>

int main()
{
	int array1[5] = {1, 2, 3, 4, 5};
	int array2[5] = {6, 7, 8, 9, 10};
	int array3[10] = {};
	int size_array1 = sizeof(array1) / sizeof(int);
	int size_array2 = sizeof(array2) / sizeof(int);
	int size_array3 = sizeof(array3) / sizeof(int);

	//printf("%d %d %d", size_array1, size_array2, size_array3);

	for(int i = 0; i < size_array1; i++)
	{
		array3[i] = array1[i];
	}
	for(int i = 0; i < size_array3; i++)
	{
		array3[size_array1 + i] = array2[i];
	}

	for (int i = 0; i < size_array3; ++i)
	{
		printf("%d ", array3[i] );
	}

	return 0;
}