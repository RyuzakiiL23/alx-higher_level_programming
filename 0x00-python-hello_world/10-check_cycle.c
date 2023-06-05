#include "lists.h"
/**
	* check_cycle - checks if there is a cycle
	* @list: pointer to the head of the list
	* Return: returns 1 if its a cycle and 0 if not
*/

int check_cycle(listint_t *list)
{
	listint_t *head, *tail;

	if (list == NULL)
	{
		return (0);
	}
	head = list;
	tail = list;

	while (tail != NULL)
	{
		tail = list->next;
		list = list->next;
		if (head == list)
		{
			return (1);
		}
	}
	return (0);
}
