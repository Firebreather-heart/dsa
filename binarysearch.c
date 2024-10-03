#include <stdio.h>

int binarysearch(int * arr, int item, int arrsize){
    int low = 0;
    int high = arrsize - 1;

    while(low <= high){
        int mid = (low+high)/2;
        int guess = arr[mid];
        if(guess == item){
            return mid;
        } else if(guess > item){
            high = mid -1;
        } else {
            low = mid + 1;
        }
    }
    return -1;
}

int main(){
    int arr[] = {1, 3, 5, 7, 9};
    int arrsize = sizeof(arr)/sizeof(arr[0]);
    int item = 3;
    int result = binarysearch(arr, item, arrsize);
    if(result == -1){
        printf("Item not found\n");
    } else {
        printf("Item found at index %d\n", result);
    }
    return 0;
}