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
	listint_t *tmp1 = *head;
	listint_t *tmp2 = *head;
	listint_t *tmp = NULL;
	listint_t *second_half = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);


	/* Find the middle node of the list */
	while (tmp2 != NULL && tmp2->next != NULL)
	{
		tmp2 = tmp2->next->next;
		tmp1 = tmp1->next;
	}

	/* If the list has an odd number of nodes, skip the middle node */
	if (tmp2 != NULL)
		tmp1 = tmp1->next;

	/* Reverse the second half of the list */
	while (tmp1 != NULL)
	{
		tmp = tmp1->next;
		tmp1->next = second_half;
		second_half = tmp1;
		tmp1 = tmp;
	}

	/* Compare the first half with the reversed second half */
	while (second_half != NULL)
	{
		if ((*head)->n != second_half->n)
			return (0);
		*head = (*head)->next;
		second_half = second_half->next;
	}

	return (1);
}
