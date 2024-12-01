#include <stdio.h>

int main() {
    int s;
    printf("Size: ");
    scanf("%d", &s);
    int arr[s];

    printf("Enter elements of array: \n");
    for (int i = 0; i < s; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Duplicate values are: ");
    for (int i = 0; i < s; i++) {
        int j;
        for (j = i + 1; j < s; j++) {
            if (arr[i] == arr[j]) {
                break;
            }
        }
        if (j != s) {
            int k;
            for (k = 0; k < i; k++) {
                if (arr[i] == arr[k]) {
                    break;
                }
            }
            if (k == i) {
                printf("%d ", arr[i]);
            }
        }
    }
    printf("\n");

    return 0;
}
