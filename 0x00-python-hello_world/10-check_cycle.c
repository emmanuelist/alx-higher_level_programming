#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head o the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
		slow  = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}
/**
 * The key ideas: - Use two pointers, slow and fast.
 * slow moves one node at a time. fast moves two nodes at a time.
 * If there is a cycyle, fast will eventually meet slow.
 * Only need to traverse the linked list once.
 * Constant memory usage - only two extra pointers.
 *
 * ******** TO OPTIMIZE **********
 * Check input for NULL before entering loop
 * Return early if fast or fast->next becomes NULL
 * Use a function like printf() or putchar() for output to avoid extra memory
 */
