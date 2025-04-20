#include <stdio.h>

int *qsort(int *arr, int arrsize);

int *qsort(int *arr, int arrsize){
    if (arrsize < 2){
        return arr;
    } else{
        int mid = arrsize/2;
        int pivot = arr[mid];
        int left[mid], right[mid];
        for (int i = 0; i < mid; i++)
        {
            left[i] = arr[i];
            right[i] = arr[i + mid];
        }
        int rsize = (arrsize % 2 == 0) ? (mid - 1): mid;
        return qsort(left, mid);
    }
}