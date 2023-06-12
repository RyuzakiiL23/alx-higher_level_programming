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
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *tmp = NULL;
	listint_t *second_half = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);


	/* Find the middle node of the list */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	/* If the list has an odd number of nodes, skip the middle node */
	if (fast != NULL)
		slow = slow->next;

	/* Reverse the second half of the list */
	while (slow != NULL)
	{
		tmp = slow->next;
		slow->next = second_half;
		second_half = slow;
		slow = tmp;
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
