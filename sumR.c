#include <stdio.h>

int sumR(int *arr, int arrsize);

int main(){
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    printf("%d\n", sumR(arr, 10));
}

int sumR(int *arr, int arrsize){
    if (arrsize == 0){
        return 0;
    } else{
        return arr[0] + sumR(arr+1, arrsize-1);
    }
}