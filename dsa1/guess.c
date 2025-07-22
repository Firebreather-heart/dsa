#include <stdio.h>

char get_user_input(int val);
int check_greater(int val);
int search_correct(int top, int btm);

int main()
{
    printf("Guess a number between 1 and 100; don't change it!!!\n");
    int correct = search_correct(100, 1);
    printf("the correct value is %i\n", correct);
}

char get_user_input(int val)
{
    printf("Is the number greater than %i, y or n, enter any other key if neither:  ", val);
    char usr_inp;
    scanf(" %c", &usr_inp);
    puts("\n");
    return usr_inp;
}

int check_greater(int val)
{
    char y_n = get_user_input(val);
    if (y_n == 'y')
    {
        return 0;
    }
    else if (y_n == 'n')
    {
        return 1;
    }
    else
    {
        return 2;
    }
}

int search_correct(int top, int btm)
{
    int guess = (top + btm) / 2;
    int cgg = check_greater(guess);
    if (cgg == 0)
    {
        btm = guess;
        return search_correct(top, btm);
    }
    else if (cgg == 1)
    {
        top = guess;
        return search_correct(top, btm);
    }
    else
    {
        return guess;
    }
}