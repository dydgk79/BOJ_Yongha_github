#include <stdio.h>

int main() {
    int a=1, b=1, c=1;

    while(1) {
        scanf("%d %d %d", &a, &b, &c);
        if(a == 0 && b == 0 && c == 0) break; // 종료 조건
        
        // a, b, c를 정렬 (a <= b <= c)
        if(a > b) { int temp = a; a = b; b = temp; }
        if(b > c) { int temp = b; b = c; c = temp; }
        if(a > b) { int temp = a; a = b; b = temp; }

        // 직각삼각형 판별
        if(a*a + b*b == c*c) {
            printf("right\n");
        } else {
            printf("wrong\n");
        }
    }
    return 0;
}
