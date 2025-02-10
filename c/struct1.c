#include <stdio.h>
typedef struct
{    
     int age;
    char name[100];
    int rank;
}student;
student registe();
int check(student p);
int main(){
    student s1;
    s1=registe();
    int p = check(s1);
    printf("Name is %s\n",s1.name);
    if (p<0)
    {
       printf("Not Eligible\n");
    }
    else printf("Eligible\n");
    
    
}
 student registe(){
    student p;
    printf("Enter name age rank");
    scanf("%s %d %d",p.name,&p.age,&p.rank);
    return p;
}
int check(student p){
    if (p.rank>3000)
    {
       return -1;
    }
    else{
        return 0;
    }
}