#include <stdio.h>
#include <stdlib.h>
#include "node.h"

struct Node* createNode(char priority) {
    struct Node* newNode = (struct Node*) malloc(sizeof(struct Node));
    newNode->number = 0;
    newNode->priority = priority;
    newNode->next = NULL;
    return newNode;
}

void serveCustomer(struct Node **head) {
    if (*head == NULL || (*head)->next == NULL) {
        printf("Empty queue!\n");
        return;
    }

    struct Node *first = (*head)->next;
    printf("Calling card customer %d (%c) for service\n", first->number, first->priority);

    (*head)->next = first->next;
    free(first);
}

void printClientList(struct Node *head)
{
    struct Node *currentNode = head->next;
    if (currentNode == NULL) {
        printf("Empty queue.\n");
        return;
    }
    while (currentNode != NULL) {
        printf("%d (%c)\n", currentNode->number, currentNode->priority);
        currentNode = currentNode->next;
    }
}

void menu(struct Node *clientList) {
    int option;
    char type;
    do {
        printf("\nMenu:\n");
        printf("1 Add client to queue\n");
        printf("2 Show queue\n");
        printf("3 Call client\n");
        printf("4 Exit\n");
        printf("Choose an option: ");
        scanf("%d", &option);

        switch(option) {
            case 1:
                printf("Enter the card type (C or P): ");
                scanf(" %c", &type);
                if (type == 'C') {
                    insertWithoutPriority(clientList, createNode('C'));
                } else if (type == 'P') {
                    insertWithPriority(clientList, createNode('P'));
                } else {
                    printf("Invalid type.\n");
                }
                break;
            case 2:
                printClientList(clientList);
                break;
            case 3:
                serveCustomer(&clientList);
                break;
            case 4:
                printf("Finishing.\n");
                break;
            default:
                printf("Invalid option. Try again.\n");
        }
    } while (option != 4);
}

int main()
{
    struct Node* clientList = (struct Node*) malloc(sizeof(struct Node));
    clientList->number = -1;
    clientList->priority = ' ';
    clientList->next = NULL;

    menu(clientList);
    
    return 0;
}