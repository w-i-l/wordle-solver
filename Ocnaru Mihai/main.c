#include <stdio.h>
#include <stdlib.h>

#define WORD_LENGHT 7 //5 litere + '\n' + '\0'
#define WORD_COUNT 11454
#define A_ASCII_INDEX (int)'A'
#define LETTERS_COUNT 26


float no_of_letters = (WORD_LENGHT-2)*WORD_COUNT;
struct Letter{
    char letter ;
    int letter_count;
}letters[LETTERS_COUNT],aux;

void sort_letters(){

    for(int i=0;i<LETTERS_COUNT;i++){
        for(int j=i+1;j<LETTERS_COUNT;j++){
            if (letters[i].letter_count < letters[j].letter_count){
                aux = letters[i];
                letters[i] = letters[j];
                letters[j] = aux;
            }
        }
    }
}

void display_letters_count(){
    for(int i=0;i<LETTERS_COUNT;i++){
        printf("%c: %d -- %f%% \n",letters[i].letter,letters[i].letter_count,letters[i].letter_count/no_of_letters*100);
    }
}


void get_letters_count(FILE *file){
    fseek(file,0,SEEK_SET);
    char c;
    while(EOF != (c=getc(file))){
        if(c!=' ' && c!='\n'){
            letters[c%A_ASCII_INDEX].letter = c;
            letters[c%A_ASCII_INDEX].letter_count ++;
        }

    }
}

void random_world(FILE *file,int seed,char *c){
    srand(seed);
    int random_number = (rand()%WORD_COUNT) * WORD_LENGHT;
    fseek(file,random_number,SEEK_SET);
    fscanf(file,"%s",c);
}

int main()
{
    FILE *f;
    f = fopen("cuvinte.txt","r");

    char c[WORD_LENGHT-1];

    random_world(f,1223,c);
    printf("%s\n",c);

    get_letters_count(f);
    display_letters_count();

    printf("\n");

    sort_letters();
    display_letters_count();

    fclose(f);
    return 0;
}
