#include <stdio.h>
int main(void)
{
int i = 0;

while (i <= 9)
{	
	putchar(i + '0');
	if (i != 9)
	{
		putchar(',');
		putchar(' ');
	}
}
putchar('\n');
return (0);
}
