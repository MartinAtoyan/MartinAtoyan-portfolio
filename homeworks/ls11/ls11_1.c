#include <stdio.h>

int main()
{
	int a = 5;
	float f = 6.35;
	char c = 'c';

	int* a_ptr = &a;
	float* f_ptr = &f;
	char* c_ptr = &c;

	//printf("%p\n%p\n%p\n", a_ptr, f_ptr, c_ptr );
	printf("%d\n", 5 );
	return 0;
}