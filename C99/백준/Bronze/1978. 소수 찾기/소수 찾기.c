#include <stdio.h>
#include <stdbool.h>

// 소수인지 판별하는 함수
bool isPrime(int n) {
    if (n <= 1) {
        return false; // 1 이하의 숫자는 소수가 아님
    }
    for (int i = 2; i * i <= n; i++) { // 제곱근까지만 확인
        if (n % i == 0) {
            return false; // 약수가 존재하면 소수가 아님
        }
    }
    return true; // 소수임
}

int main() {
    int N,T;
    int ans = 0;
    scanf("%d\n",&N);
    while(N>0) {
        scanf("%d ",&T);
            if (isPrime(T)) {ans++;}
        N--;
    }
    printf("%d",ans);
}