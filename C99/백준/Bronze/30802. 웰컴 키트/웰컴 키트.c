#include <stdio.h>

int main() {
    int N, S, M, L, XL, XXL, XXXL, T, P;
    int AT = 0, AP = 0, APP = 0;

    // 입력 받기
    scanf("%d %d %d %d %d %d %d %d %d", &N, &S, &M, &L, &XL, &XXL, &XXXL, &T, &P);

    // 각 사이즈별로 T만큼 줄어든 총 개수 계산
    AT += (S + T - 1) / T; // 올림 계산
    AT += (M + T - 1) / T;
    AT += (L + T - 1) / T;
    AT += (XL + T - 1) / T;
    AT += (XXL + T - 1) / T;
    AT += (XXXL + T - 1) / T;

    // N을 P로 나눈 몫과 나머지 계산
    AP = N / P;
    APP = N % P;

    // 결과 출력
    printf("%d\n", AT);
    printf("%d %d\n", AP, APP);

    return 0;
}
