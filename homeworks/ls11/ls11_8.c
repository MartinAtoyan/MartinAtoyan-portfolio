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
	int max = array[0];
	for(int i = 1; i < n; ++i)
	{
		if (max < array[i])
		{
			max = array[i];
		}
	}
	printf("%d\n", max);
	return 0;
}