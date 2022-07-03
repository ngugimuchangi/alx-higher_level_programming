#include "lists.h"
/**
 * reverse - reverse linked list
 * @head: head of the list
 *
 * Return: nothing
 */
void reverse(listint_t **head)
{
	listint_t *current, *prev = NULL, *next;

	current = *head;
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: address of the first node
 *
 * Return: 1 if palindromic, else 0.
 */
int is_palindrome(listint_t **head)
{
	int len, i, j;
	listint_t *temp, *temp_mid;

	temp = *head;
	if (!temp || !temp->next)
		return (1);
	for (len = 0; temp; len++, temp = temp->next)
		;
	temp_mid = *head;
	j = (len % 2 == 0) ? (len / 2) : (len / 2) + 1;
	for (i = 0; i < j; i++)
		temp_mid = temp_mid->next;
	reverse(&temp_mid);
	temp = *head;
	for (i = 0; i < j - 1; i++)
	{
		if (temp->n != temp_mid->n)
			return (0);
		temp = temp->next;
		temp_mid = temp_mid->next;
	}
	return (1);
}
