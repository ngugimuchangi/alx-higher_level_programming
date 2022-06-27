#include "lists.h"

/**
 * check_cycle - checks for cycles
 * @list: start of the linked list
 *
 * Description: checks if a singly linked list
 * has a loop/cycle
 *
 * Return: 0 if no cycle, 1 if there's a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *temp2;

	if (!list)
		return (0);
	temp = list;
	temp2 = list->next;

	while (temp != NULL && temp2 != NULL)
	{
		if (temp == temp2)
			return (1);
		if (!temp2->next)
			return (0);
		temp = temp->next;
		temp2 = temp2->next->next;
	}
	return (0);
}
