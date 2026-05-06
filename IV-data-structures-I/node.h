struct Node {
    int number;
    char priority;
    struct Node *next;
};

void insertWithoutPriority(struct Node *head, struct Node *newNode);
void insertWithPriority(struct Node *head, struct Node *newNode);