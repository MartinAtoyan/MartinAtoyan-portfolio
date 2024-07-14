#include <stdio.h>

int main()
{
    int number;
    scanf("%d", &number);
    int n;
    scanf("%d", &n);
    int index = 1 << n;
    number = number * index;
    printf("%d", number);
    
    

    return 0;
}
