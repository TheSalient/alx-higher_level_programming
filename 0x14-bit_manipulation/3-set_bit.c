#include "main.h"

/**
 * set_bit - the function that sets the value of a bit to 1
 * @n: the first parameter.
 * @index: the second parameter.
 *
 * Return: int return value.
 */
int set_bit(unsigned long int *n, unsigned int index)
{
if (index > 63)
{
return (-1);
}
*n = ((1UL << index) | *n);

return (1);
}
