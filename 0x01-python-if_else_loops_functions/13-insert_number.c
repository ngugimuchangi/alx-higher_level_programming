#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - creates a new node in a sorted list
 * @head: address of start of the list
 * @number: number to add
 *
 * Return: address of new node on success, NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp = NULL, *temp2 = NULL;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!(*head))
	{
		*head = new;
		return (new);
	}
	temp = *head;
	while (temp && temp->n < number)
	{
		temp2 = temp;
		temp = temp->next;
	}
	if (!temp2)
	{
		*head = new;
		new->next = temp;
		return (new);
	}
	temp2->next = new;
	new->next = temp;
	return (new);
}
