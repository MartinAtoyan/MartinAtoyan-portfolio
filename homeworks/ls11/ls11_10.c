#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);
	if(n > 12)
	{
        while (n != 0)
        {
            printf("%d", n % 10);
            n = n / 10;
        }
	}
	
	return 0;
}