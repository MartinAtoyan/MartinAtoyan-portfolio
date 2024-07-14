#include <stdio.h>

int main()
{
    int number;
    scanf("%d", &number);
    int max_size = 8 * sizeof(int);
    int count_one = 0;
    int count_zero = 0;
    int index = 1;
    
    for(int i = 0; i < max_size; i++)
    {
        if(number & index)
            count_one++;
        else
            count_zero++;
        index <<= 1;
    }
    
    printf("%d %d", count_zero, count_one);
    
    

    return 0;
}
