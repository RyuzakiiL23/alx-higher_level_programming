#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{

	(*head)->n = number;

	return(*head);
}
