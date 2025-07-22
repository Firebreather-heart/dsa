#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};

struct Node *createNode(int data);
void insertNode(struct Node **head, int data);
void printList(struct Node *head);

int main()
{
    struct Node *list = NULL;
    insertNode(&list, 10);
    insertNode(&list, 20);
    insertNode(&list, 30);
    insertNode(&list, 40);

    printList(list);
}

struct Node *createNode(int data)
{
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));

    if (newNode == NULL)
    {
        puts("Memory allocation failed");
        exit(EXIT_FAILURE);
    }

    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void insertNode(struct Node **head, int data)
{
    struct Node *new = createNode(data);
    if (*head == NULL)
    {
        *head = new;
    }
    else
    {
        struct Node *current = *head;
        while (current->next != NULL)
        {
            current = current->next;
        }
        current->next = new;
    }
}

void removeNode(struct Node **head){
    /* check if the list is empty */
    if (*head == NULL){
        puts("List is empty");
    } else {
        struct Node *prev = NULL;
        struct Node *current = *head;
        while (current->next != NULL){
            prev = current;
            current = current->next;
        }
        if (prev == NULL){
            free(current);
            *head = NULL;
        } else{
            prev->next = NULL;
            free(current);
        }
    }
}

void printList(struct Node *head){
    if (head == NULL){
        puts("[ ]");
    } else{
        printf("[");
        while (head != NULL){
            printf("%d, ", head->data);
            head = head->next;
        }
        puts("\b\b]");
    }
}