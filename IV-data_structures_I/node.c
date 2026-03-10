#include <stdio.h>
#include <stdlib.h>
#include "node.h"

void insertWithoutPriority(struct Node *head, struct Node *newNode)
{
    struct Node *currentNode = head;
    int count = 1;

    while (currentNode->next != NULL)
    {
        currentNode = currentNode->next;
    }

    if (currentNode->priority == 'C') {
        count = currentNode->number + 1;
    }

    newNode->number = count;
    currentNode->next = newNode;
    newNode->next = NULL;
}

void insertWithPriority(struct Node *head, struct Node *newNode)
{
    struct Node *currentNode = head;
    int count = 301;    

    while(currentNode->next != NULL && currentNode->next->priority == 'P')
    {
        currentNode = currentNode->next;
        count++;
    }

    struct Node *next = currentNode->next;
    newNode->number = count;
    newNode->next = next;
    currentNode->next = newNode;
}