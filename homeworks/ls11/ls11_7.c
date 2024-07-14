#include <stdio.h>
#include <stdlib.h>

int main()
{
    char *str;
    int n;
    scanf("%d", &n); 
    str = (char*)malloc(n*sizeof(char));
    for(int i = 0; i < n; i++)
    {
        scanf(" %c", str + i); 
    }

	for(int i = 0; str[i] != '\0'; i++)
	{
		if (str[i] >= 'a' && str[i] <= 'z')
		{
            str[i] = str[i] - 'a' + 'A';
        }
	}
	printf("%s\n", str);
}