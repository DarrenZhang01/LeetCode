/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode * AddTwoNumbers (struct ListNode * l1, struct ListNode * l2) {
	struct ListNode *new_l, *p;
	new_l = malloc(sizeof(struct ListNode));
	// Let the pointer p  keep track of the nodes of new_l
	p = new_l;
	int carry_out = 0;
	
	// Construct new node if the while condition is True
	while (l1 != NULL || l2 != NULL) {
		
		int digit = 0;
		int a, b;
		// Initialize the values of a & b
		if (l1) {
			a = l1->val;
		} else {
			a = 0;
		}
		if (l2) {
			b = l2->val;
		} else {
			b = 0;
		}
		
		digit = a + b + carry_out;
		carry_out = digit / 10;
		p->next = malloc(sizeof(struct ListNode));
		p = p->next;
		p->val = digit % 10;
		if (l1) {
			l1 = l1->next;
		}
		if (l2) {
			l2 = l2->next;
		}
	}
	if (carry_out > 0) {
		p->next = malloc(sizeof(struct ListNode));
		p = p->next;
		p->val = carry_out;
	}
	p->next = NULL;
	return new_l->next;
}
