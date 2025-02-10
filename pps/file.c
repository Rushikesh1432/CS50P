#include <stdio.h>
typedef struct address{
    int hno;
    int block;
    char city[20];
    char state[20];
}add;
int main(){
    add p[4]={{1,21,"hyd","TG"},
    {2,22,"deli","dili"},
    {3,23,"bombay","maha"},
    {4,24,"pune","maha"},};

    FILE* f;
    f=fopen("file.bin","wb+");
    fwrite(p,sizeof(add),4,f);
    rewind(f);
    add read[4];
    fread(read,sizeof(add),4,f);
    for(int i=0;i<4;i++){ 
    printf("%d\n",read[i].hno);
    printf("%d\n",read[i].block);
    printf("%s\n",read[i].state);
    printf("%s\n",read[i].city);
    printf("\n");}

}
