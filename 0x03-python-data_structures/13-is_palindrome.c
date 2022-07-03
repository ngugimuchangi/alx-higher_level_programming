#include "lists.h"
/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: address of the first node
 *
 * Return: 1 if palindromic, else 0.
 */
int is_palindrome(listint_t **head)
{
	int len, len_cpy, i, j;
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
	len_cpy = (len / 2) - 1;
	for (i = 0; i < (len / 2) - 1; i++)
	{
		for (j = 0, temp = *head; j < len_cpy; j++)
			temp = temp->next;
		if (temp->n != temp2->n)
			return (0);
		len_cpy--;
		temp2 = temp2->next;
	}
	return (1);
}
