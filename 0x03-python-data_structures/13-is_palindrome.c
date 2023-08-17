#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * reverse_listint - reverses the listint_t list, a singly linked list
 * @head: pointer to the head of the reversed list
 *
 * Return: ptr to head of reversed list
 */ 
listint_t *reverse_listint(listint_t **head)
{
	listint_t *current = *head, *next_node, *previous = NULL;

	while (current)
	{
		next_node = current->next;
		current->next = previous;
		previous = current;
		current = next_node;
	}
	*head = previous;
	return (*head);
}
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *reversed_half, *midpoint;
	size_t size = 0, j;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	
	current = *head;
	while (current)
	{
		size++;
		current = current->next;
	}
	
	current = *head;
	for (j = 0; j < (size / 2) - 1; j++)
		current = current->next;
	
	if ((size % 2) == 0 && current->n != current->next->n)
		return (0);
	
	current = current->next->next;
	reversed_half = reverse_listint(&current);
	midpoint = reversed_half;
	
	current = *head;
	while (reversed_half)
	{
		if (current->n != reversed_half->n)
			return (0);
		current = current->next;
		reversed_half = reversed_half->next;
	}
	reverse_listint(&midpoint);
	return (1);
}
