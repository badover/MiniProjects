#include<stdio.h>

void convertTime(int totalSecond, int *hours, int *minutes, int *seconds){
    *hours = totalSecond / 3600;
    totalSecond %= 3600;
    *minutes = totalSecond / 60;
    *seconds = totalSecond % 60;
}

int main() {

    int totalSecond;
    int hours, minutes, seconds;

    scanf("%d", &totalSecond);

    convertTime(totalSecond, &hours, &minutes, &seconds);

    printf("%dseconds = %d hours, %d minutes, %d seconds", totalSecond, hours, minutes, seconds);

    return 0;
}
