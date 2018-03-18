#include <stdio.h>
#include <omp.h>
#include <time.h>
#include <stdlib.h>
#include <malloc.h>


int getMemory(int number_of_points) {
	return number_of_points * sizeof(int);
}

void initPositions(int *positions, int number_of_points, int start_position) {
	for (int i = 0; i < number_of_points; i++) {
        positions[i] = start_position;
    }
}

void initRandoms(int *randoms, int number_of_points) {
	for (int i = 0; i < number_of_points; i++) {
        randoms[i] = rand();
    }
}

int isProbability(int z, int p) {
	return (double)z / RAND_MAX <= p;
}

int isPositionInSegment(int position, int left, int right) {
	return position > left && position < right;
}

void addResultToFile(int result, int number_of_points, 
					int time, double finish, double start, int left, 
					int right, int start_position, double p, 
					int number_of_thread) {
	FILE *file;
    file = fopen("stats.txt", "a");

    fprintf(file, "%f %f %fs ", 
			(double)result / number_of_points,
			(double)time / number_of_points, 
			finish - start);
    fprintf(file, "%d %d %d %d %f %d\n", 
			left, right, 
			start_position, number_of_points, p, number_of_thread);

    fclose(file);
    
}

void changePosition(int *position, int z, int p) {
	if (isProbability(z, p)) {
    	++(*position);
    } else {
        --(*position);
    }
}

int isRight(int position, int right) {
	return position == right;
}


int main(int argc, char *argv[]) {
    srand(time(NULL));
	const int NUMBER_OF_ARGUMENT_FOR_MAIN = 7;
    const int ERROR_INCORRECT_ARGUMENT = 1;
    if (argc != NUMBER_OF_ARGUMENT_FOR_MAIN) {
        exit(ERROR_INCORRECT_ARGUMENT);
    }
    int left = atoi(argv[1]), right = atoi(argv[2]);
    int start_position = atoi(argv[3]);
    int number_of_points = atoi(argv[4]);
    double p = atof(argv[5]);
    int number_of_thread = atoi(argv[6]);
    int result = 0, time = 0;
    int *randoms = (int *)malloc(getMemory(number_of_points));
    int *positions = (int *)malloc(getMemory(number_of_points));

	initRandoms(randoms, number_of_points);
    initPositions(positions, number_of_points, start_position);

    double start = omp_get_wtime();
#pragma omp parallel for num_threads(number_of_thread) reduction (+: time) reduction (+: result)
    for (int i = 0; i < number_of_points; i++) {
        int z = randoms[i];
        while (isPositionInSegment(positions[i], left, right)) {
            ++time;
			changePosition(&positions[i], z, p);
            z = rand_r(&z);
        }
        if (isRight(positions[i], right)) {
            ++result;
        }
    }
    double finish = omp_get_wtime( );

	addResultToFile(result, number_of_points, time, finish, start, left,  right, start_position, p, number_of_points);

    free(positions);
    free(randoms);
    return 0;
}
