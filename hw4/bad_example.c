#include <stdio.h>
#include <omp.h>
#include <time.h>
#include <stdlib.h>
#include <malloc.h>


int main(int argc, char *argv[]) {
    if (argc != 7) {
        exit(1);
    }
    int a = atoi(argv[1]), b = atoi(argv[2]);
    int x = atoi(argv[3]);
    int N = atoi(argv[4]);
    double p = atof(argv[5]);
    int num_th = atoi(argv[6]);

    srand(time(NULL));
    int *ran = (int *)malloc(N * sizeof(int));
    for (int i = 0; i < N; i++) {
        ran[i] = rand();
    }

    int res = 0, time = 0;
    int *pos = (int *)malloc(N * sizeof(int));

    FILE *file;
    file = fopen("stats.txt", "a");

    double ts1 = omp_get_wtime( );
#pragma omp parallel for num_threads(num_th) reduction (+: time) reduction (+: res)
    for (int i = 0; i < N; i++) {
        int z = ran[i];
        pos[i] = 0;
        while ((pos[i] > a - x) && (pos[i] < b - x)) {
            time += 1;

            if (1. * z / RAND_MAX <= p) {
                pos[i] += 1;
            } else {
                pos[i] -= 1;
            }

            z = rand_r(&z);
        }

        if (pos[i] == b - x) {
            res += 1;
        }
    }
    double ts2 = omp_get_wtime( );

    fprintf(file, "%f %f %fs ", 1. * res / N, 1. * time / N, ts2 - ts1);
    fprintf(file, "%d %d %d %d %f %d\n", a, b, x, N, p, num_th);

    fclose(file);
    free(pos);
    free(ran);
    return 0;
}
