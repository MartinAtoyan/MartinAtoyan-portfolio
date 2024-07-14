#include <stdio.h>

int main()
{
	int array1[5] = {1, 2, 3, 4, 5};
	int array2[5] = {6, 7, 8, 9, 10};
	int size_array = sizeof(array1) / sizeof(int);
	int count = 0;

	for (int i = 0; i < size_array; ++i)
	{
		if (array1[i] == array2[i])
		{
			count++;
		}
	}

	if(count == size_array)
	{
		printf("They are equal");
	}
	else
	{
		printf("They aren't equal\n");
	}
	return 0;
}