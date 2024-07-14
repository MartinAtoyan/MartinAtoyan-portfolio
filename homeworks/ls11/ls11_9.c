#include <stdio.h>
#include <stdlib.h>

int main()
{
	int *array;
	int n;
	scanf("%d", &n);
	array = (int*)malloc(n * sizeof(int));
	for (int i = 0; i < n; ++i)
	{
		scanf("%d", &array[i]);
	}
	int min = array[0];
	for(int i = 1; i < n; ++i)
	{
		if (min > array[i])
		{
			min = array[i];
		}
	}
	printf("%d\n", min);
	return 0;
}