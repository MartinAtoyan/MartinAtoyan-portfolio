#include <stdio.h>

int main()
{
	int number = 10;
	int n;
	scanf("%d", &n);
	int index = 1 << n;
	if (number & index)
		printf("1");
	else
		printf("0");

	return 0;
}


