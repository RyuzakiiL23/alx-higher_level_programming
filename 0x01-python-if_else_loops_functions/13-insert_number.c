#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *tmp = *head;

	if (new == NULL)
		return (NULL);

	new->n = number;

	if (tmp == NULL || tmp->n >= number)
	{
		new->next = tmp;
		*head = new;
		return (new);
	}

	while (tmp->next != NULL && tmp->next->n < number)
	{
		tmp = tmp->next;
	}
	new->next = tmp->next;
	tmp->next = new;

	return (new);
}
