#include <stdio.h>

/*
 n is the end number, the sum runs from 1 to the end number
*/
int intpow(int x, int n);

int main(){
    int a, b;
    printf("enter two numbers   a b   to get the power a ^ b:  ");
    scanf("%d %d", &a, &b);
    printf("%d\n", intpow(a, b));
}

int intpow(int x, int n){
    if (x <= 0){
        return 0;
    } else if (n == 0){
        return 1;
    }
    else if (n > 0){
        n -= 1;
        return x * intpow(x, n);
    }
    return x;
}