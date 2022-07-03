#include "lists.h"
/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: address of the first node
 *
 * Return: 1 if palindromic, else 0.
 */
int is_palindrome(listint_t **head)
{
	int len, i;
	listint_t *temp, *temp2;

	temp = *head;
	if (!temp || !temp->next)
		return (1);
	for (len = 0; temp; len++, temp = temp->next)
		;
	temp2 = *head;
	if (len % 2 == 0)
		for (i = 0; i < (len / 2); i++, temp2 = temp2->next)
			;
	else
		for (i = 0; i < (len / 2 + 1); i++, temp2 = temp2->next)
			;
	temp = *head;
	for (i = 0; i < (len / 2) - 1; i++)
	{
		if (temp->n != temp2->n)
			return (0);
		temp = temp->next;
		temp2 = temp2->next;
	}
	return (1);
}
