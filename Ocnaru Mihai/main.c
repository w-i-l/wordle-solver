#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define WORD_LENGHT 7 //5 litere + '\n' + '\0'
#define WORD_COUNT 11454
#define A_ASCII_INDEX (int)'A'
#define LETTERS_COUNT 26


float no_of_letters = (WORD_LENGHT-2)*WORD_COUNT;

char enter_word[6];//cuvantul introdus de noi
char chosen_word[WORD_LENGHT-1];//cuvantul ales de pc
char word[6];//array folosit pt stocare
char good_letters[6];//literele care apar in enter_word
int index_good_letters = 0;
char bad_letters[26];//literele care nu apar in enter_word
int index_bad_letters = 0;
char word_structure[6];//daca o litera apare pe locul potrivit


//structura de stocare a literelor din fisier
struct Letter{
    char letter ;
    int letter_count;
    int first_index;
}letters[LETTERS_COUNT],aux;


//verificarea existentei unui cuvant in fisier
//returneaza 1 daca exita
//returneaza 0 daca nu exista
int word_exist(FILE *file){

    //setam mereu pozitia cursorului la inceput
    fseek(file,0,SEEK_SET);
    //stocam cuvantul curent
    char current_word[6];

    //parcurgem pana gasim cuvantul sau EOF
    while(fgets(current_word,6,file) && strcmp(current_word,word)) {}

    //verificam daca am gasit cuvantul
    if(strcmp(current_word,word)==0){

        return 1;
    }
    return 0;



}

//verifica daca o litera sa afla in word sau nu
//returneaza 1 daca da
//returneaza 0 daca nu
int is_not_letter_duplicated(int index){
    for(int i=0;i<index;i++){
        if(word[i] == word[index]){
            return 0;
        }
    }
    return 1;

}

//genereaza toate anagramele cuvantului stocat in word
//foloseste backtrack
void generate_all_anagrams(FILE *file,int index){
    //iteram peste pozitiile din word
    //indexul este pozitia curenta din word
    for(int i=0;i<5;i++){

        word[index] = letters[i].letter;

        //daca nu se repeta litera
        if(is_not_letter_duplicated(index)){
            //daca backtracul este complet
            //avem un cuvant din 5 litere
            if(index==4 ){
                    //verificam existenta cuvantului in fisier
                    if(word_exist(file)){
                        //luam ultimul cuvant existent
                        strcpy(enter_word,word);
                    }
            }
            //continuam backtracul
            else{

                    generate_all_anagrams(file,index+1);

                }

        }

    }
}


//sorteaza structura letters dupa probabilitatea de aparitie a literei
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

//afisare formatata a structurii letters
void display_letters_count(){
    for(int i=0;i<LETTERS_COUNT;i++){
        printf("%c: %d -- %f%% index:%d \n",letters[i].letter,letters[i].letter_count,letters[i].letter_count/no_of_letters*100,
                                                                                                letters[i].first_index);
    }
}

//numara aparitia fiecarei litere din fisier
//le stocheaza in structura letters
void get_letters_count(FILE *file){
    //seteaza cursorul la inceput
    fseek(file,0,SEEK_SET);
    char c;
    //iteram tot fisierul
    while(EOF != (c=getc(file))){
        if(c!=' ' && c!='\n'){
            letters[c%A_ASCII_INDEX].letter = c;
            letters[c%A_ASCII_INDEX].letter_count ++;
            //to find first index at the start of the word of the letters in txt
            //cuvintele sunt stocate pe 7 bytes incepand de la index 1
            if(ftell(file)%7==1 && letters[c%A_ASCII_INDEX].first_index == 0){
                   letters[c%A_ASCII_INDEX].first_index = ftell(file);
            }
        }
    }
}

//alege un cuvant random din fisier bazat pe un seed
void random_world(FILE *file,int seed,char *c){

    srand(seed);
    int random_number = (rand()%WORD_COUNT) * WORD_LENGHT;
    fseek(file,random_number,SEEK_SET);
    fscanf(file,"%s",c);
}

//stocheza in bad/good letters literele pe care l/nu le vom folosi in continuare
void check_letters(FILE *file){
    //iteram peste cuvantul introdus si compara literele cu cele de la cuvantul ales de pc
    for(int index_chosen_word=0;index_chosen_word<5;index_chosen_word++){
        for(int index_enter_word=0;index_enter_word<5;index_enter_word++){
            if(enter_word[index_enter_word] == chosen_word[index_chosen_word]){
                int can_add = 1;

                for(int i=0;i<index_good_letters;i++){
                    if(enter_word[index_enter_word] == good_letters[i]){//daca exista deja litera
                        can_add = 0;
                        break;
                    }
                }

                if(can_add){
                    good_letters[index_good_letters] = enter_word[index_enter_word];
                    index_good_letters++;
                }
                if(index_chosen_word == index_enter_word){//daca sunt pe aceeasi pozitie{
                    word_structure[index_chosen_word] = enter_word[index_chosen_word];

                }
            }

        }
    }

    for(int index_enter_word=0;index_enter_word<5;index_enter_word++){//adaugare bad letters
        int can_be_added = 1;//daca nu e in good_letters
        for(int i=0;i<index_good_letters;i++){
            if(enter_word[index_enter_word] == good_letters[i]){//daca litera e buna
                    can_be_added = 0;
            }
        }

        if(can_be_added){
            int can_add = 1;

            for(int j=0;j<index_bad_letters;j++){
                if(enter_word[index_enter_word] == bad_letters[j]){//daca exista deja litera
                    can_add = 0;
                    break;
                }
            }

            if(can_add){
                bad_letters[index_bad_letters] = enter_word[index_enter_word];
                index_bad_letters++;
            }
        }
    }
}

void display_good_letters(){

    printf("Good Letters:\t");
    for(int i=0;i<index_good_letters;i++){
        printf("%c ",good_letters[i]);
    }
    printf("\n");
}

void display_bad_letters(){
    printf("Bad Letters:\t");
    for(int i=0;i<index_bad_letters;i++){
        printf("%c ",bad_letters[i]);
    }
    printf("\n");
}

void display_word_structure(){
    printf("Word structure:\t");
    for(int i=0;i<5;i++){
        printf("%c ",word_structure[i]? word_structure[i]:'_');
    }
    printf("\n");
}

//initializeaza cu valori nule structure letters
void empty_letters(){
    for(int i=0;i<LETTERS_COUNT;i++){
        letters[i].first_index = 0;
        letters[i].letter = i+A_ASCII_INDEX;
        letters[i].letter_count = 0;
    }
}

//verifiaca daca cuvantul are litere fixate
//returneaza indicele primei litere fixate
//sau -1 daca nu exista
int does_word_have_structure(){
    for(int i=0;i<5;i++){
        if(word_structure[i]!=0){
            return i;
        }
    }
    return -1;
}

////refa-o !!!!!!!!!!!!!!!!!!!!!!!!!!!!
void get_letters_count_pro(FILE *file){


    fseek(file,0,SEEK_SET);
    //creem o variabila pentru a stoca valoarea
    int does_word_have_structure_variable = does_word_have_structure();

    //mutam cursorul la pozitia initiala
    //daca gasim o litera fixata
    if(does_word_have_structure_variable != -1){
        //schimbam offsetul la indexul primei litere fixate
        //daca structura cuvantului este __R__ mutam offesetul la 2
        //indicele lui R
        fseek(file,does_word_have_structure_variable,SEEK_SET);

    }
    char c,l;
    //iteram tot fisierul
    while(EOF != (c=getc(file))){
        if(c!=' ' && c!='\n'){
            //daca litera din cuvantul curent este aceeasi
            //cu cea din structura cuvantului cautat
            if(c == word_structure[does_word_have_structure_variable]){
                //ne mutam la inceputul cuvantului
                fseek(file,-does_word_have_structure_variable-1,SEEK_CUR);

                //daca cuvantul prezent are aceasi structura ca cel ales
                int can_continue = 1;

                //verificam structura cuvantului prezent
                for(int i=0;i<5;i++){
                    if(word_structure[i] != 0 && (l=getc(file))==word_structure[i] && l!='\n'){
                        continue;
                    }
                    else{
                        //nu am gasit aceeasi structura
                        can_continue = 0;
                        break;
                    }
                }

                //daca cuvantul ales are aceeasi structura
                if(can_continue){
                    //mutam cursorul la inceputul cuvantului
                    fseek(file,-6,SEEK_CUR);

                    for(int i=0;i<5;i++){
                        //luam litera curenta
                        l = getc(file);
                        letters[l%A_ASCII_INDEX].letter_count++;

                    }

                }
            }



//            letters[c%A_ASCII_INDEX].letter = c;
//            letters[c%A_ASCII_INDEX].letter_count ++;
//            //to find first index at the start of the word of the letters in txt
//            //cuvintele sunt stocate pe 7 bytes incepand de la index 1
//            if(ftell(file)%7==1 && letters[c%A_ASCII_INDEX].first_index == 0){
//                   letters[c%A_ASCII_INDEX].first_index = ftell(file);
//            }
        }
        //parcurge din cuvant in  cuvant
        fseek(file,6,SEEK_CUR);

    }

}


int main()
{
    FILE *file;
    file = fopen("cuvinte.txt","r");



    //alegem cuvantul
    //2371263127673
    random_world(file,1234344554,chosen_word);
    printf("Choosen_Word: %s\n\n",chosen_word);

    //calculam probabilitatea
    get_letters_count(file);
    display_letters_count();
//
//    printf("\n");

    //le sortam in functie de prob
    sort_letters();
//    display_letters_count();

    //gasim toate cuv cu aceleasi litere
    generate_all_anagrams(file,0);

    printf("----------------\nEnter_word: %s\n\n",enter_word);

    check_letters(file);

    display_good_letters();
    display_bad_letters();
    display_word_structure();

    get_letters_count_pro(file);

    printf("----------------\n%d\n",does_word_have_structure());

    empty_letters();

    get_letters_count_pro(file);

    display_letters_count();


    fclose(file);
    return 0;
}
