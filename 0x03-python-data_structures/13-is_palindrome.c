#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Double pointer to the head of the list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	int count = 0, i = 0, j = 0;
	listint_t *tmp = *head;
	listint_t *tail = NULL;
	listint_t *tmp2 = NULL;
	listint_t *tail2 = NULL;

	if (*head == NULL)
		return (0);

	while (tmp != NULL)
	{
		count++;
		tail = tmp;
		tmp = tmp->next;
	}

	if ((*head)->n != tail->n)
		return (0);

	tmp = *head;

	while (i < (count + 1) / 2)
	{
		tmp2 = tmp;
		tail2 = tmp;

		for (; j < count - 2 * i - 1; j++)
			tmp2 = tmp2->next;

		if (tmp2->n != tail2->n)
			return (0);

		tmp = tmp->next;
		i++;
	}

	return (1);
}
