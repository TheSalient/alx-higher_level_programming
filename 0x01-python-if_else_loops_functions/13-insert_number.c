#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - a function
 * @head: the list head
 * @number: the number
 *
 * Return: NULL or the.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *ptr1, *ptr2, *the;
    
    the = malloc(sizeof(listint_t));

    if (the == NULL)
    {
        return (NULL);
    }
    the->n = number;

    if (head == NULL)
    {
        return (the);
    }

    ptr1 = *head;
    while ((ptr1->n < number) && ptr1->next != NULL)
    {
        ptr2 = ptr1;
        ptr1 = ptr1->next;
    }

    if (ptr1->next == NULL)
    {
        ptr1->next = the;
    }
    else if (ptr2 == *head)
    {
        if (ptr2->n < the->n)
        {
            ptr2->next = the;
        }
        else
        {
            the->next = ptr2;
        }
    }
    else
    {
        ptr2->next = the;
        the->next = ptr1;
    }
    return (the);
}
