#include "dlistint.h"

/**
 * delete_dnodeint_at_index - deletes the node at index of a dlistint_t list
 * @head: pointer to pointer of head of list
 * @index: index of the node to delete (starting at 0)
 * Return: 1 if it succeeded, -1 if it failed
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *save;
	unsigned int i;

	if (head == NULL || *head == NULL)
		return (-1);

	save = *head;
	i = 0;
	while (i < index)
	{
		*head = (*head)->next;
		if (*head == NULL)
		{
			*head = save;
			return (-1);
		}
		i++;
	}

	if ((*head)->prev != NULL)
		(*head)->prev->next = (*head)->next;
	else
		save = (*head)->next;

	if ((*head)->next != NULL)
		(*head)->next->prev = (*head)->prev;

	free(*head);
	*head = save;
	return (1);
}
