#include <stdio.h>

int main() {
    int a;
    int temp = 1;
    scanf("%d",&a);
    for(int b=a;b>0;b--) {
        temp = temp*b;
    }
    printf("%d",temp);
    return 0;
}