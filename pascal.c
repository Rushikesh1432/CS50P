#include <stdio.h>
void main(){
int a,b=0,i=1,h;
printf("Enter the number of rows: ");
scanf("%d",&h);
while(i<=h){
    b=0;
    while (b<h-i){
        printf(" ");
       b++;
    }
    a=0;b=0;
    int nb=(i-1)-b,temp=i-1,temp2,temp1; 
    while(a<i){ 
        temp2 = nb,temp1=b;int fn=1; 
        while(temp>0){ 
        fn=fn*temp;  
        temp--;
        }
       int fr=1;
        while(temp1>0){
        fr=fr*temp1; 
        temp1--;
        }
       int fnr=1;
        while(temp2>0){ 
        fnr=fnr*temp2; 
        temp2--;
        }
        int ncr = (fn)/(fr*fnr);
        printf(" %d",ncr);
        a++; b++; nb=(i-1)-b; temp=i-1;    
    }
    printf("\n");
    i++;
}
 }