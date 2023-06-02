#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    while (1) {
        int max_height = 0;
        int max_index = 0;

        for (int i = 0; i < 8; i++) {
            int mountain_h;
            scanf("%d", &mountain_h);

            if (mountain_h > max_height) {
                max_height = mountain_h;
                max_index = i;
            }
        }

        printf("%d\n", max_index);
        fflush(stdout);
    }

    return 0;
}
