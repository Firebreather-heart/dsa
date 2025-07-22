#include <stdio.h>

float get_mean(int *arr, int size);

int main()
{
    int arr[5] = {1, 2, 867, 2, 3};
    printf("mean = %.2f\n", get_mean(arr, 5));
}

float get_mean(int *arr, int size){
    float sum = 0;
    for (int i = 0; i < size; i++){
        sum += arr[i];
    }
    return sum / size;
}
