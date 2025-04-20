#include <stdio.h>

int findSmallest(int *arr, int arrsize);
int *selectionSort(int *arr, int arrsize);
void printArr(int *arr, int arrsize);

int main()
{
    int arr[] = {3, 2, 4, 1, 5, 8};
    int size = sizeof(arr) / sizeof(int);
    selectionSort(arr, size);
    printArr(arr, size);
}

/*
  returns the index of the smallest item in the list
*/
int findSmallest(int *arr, int arrsize)
{
    int least = arr[0];
    int idx = 0;
    for (int i = 1; i < arrsize; i++)
    {
        if (arr[i] < least)
        {
            least = arr[i];
            idx = i;
        }
    }
    return idx;
}

int *selectionSort(int *arr, int arrsize)
{
    for (int i = 0; i < arrsize; i++)
    {
        int smallest = i + findSmallest(arr + i, arrsize - i); // arr + i is the subarray starting from index i
        int temp = arr[i];
        arr[i] = arr[smallest];
        arr[smallest] = temp;
    }
    return arr;
}

void printArr(int *arr, int arrsize)
{
    for (int i = 0; i < arrsize; i++)
    {
        printf("%d ", arr[i]);
    }
    putchar('\n');
}