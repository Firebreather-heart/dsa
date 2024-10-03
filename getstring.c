#include "getstring.h"
#include <stdlib.h>

int main(){
    while(1){
        char name[10];
        getstring("enter messsage:  ", name);
        printf("%s\n", name);
    }
}

void getstring(char *msg, char *buf){
    printf("%s", msg);
    size_t n = 1024;
    getline(&buf, &n, stdin);
}