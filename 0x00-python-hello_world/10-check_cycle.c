#include "lists.h"

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
		if(head == list)
		{
			return (1);
		}
	}
	return (0);
}
