#include <stdio.h>
#include <math.h>


#define NUM_POINTS 1000


// returns dot product of two vectors
int dot(int *vec1, int *vec2, int len){
    int result = 0;

    for (int i=0; i<len; i++){
        result += vec1[i] * vec2[i];
    }

    return result;
}


// returns norm of a vector
int norm_square(int *vec, int n){
    int result = 0;

    for (int i=0; i<n; i++){
        result += pow(vec[i], 2);
    }

    return result;
}


// writes points of lines to plot on 3d graph
void write_data(int *m, int *n){
    FILE *f = fopen("data.txt", "w");
    int start = -10;
    int end = -start;
    double diff = end - start;

    double x, y, z;

    for (int i=0; i<=NUM_POINTS; i++){
        x = start + i*diff/NUM_POINTS;
        y = x * m[1] / m[0];
        z = x * m[2] / m[0];
        fprintf(f, "%lf %lf %lf\n", x, y, z);
    }

    for (int i=0; i<=NUM_POINTS; i++){
        x = start + i*diff/NUM_POINTS;
        y = x * n[1] / n[0];
        z = x * n[2] / n[0];
        fprintf(f, "%lf %lf %lf\n", x, y, z);
    }

    fclose(f);
}


int main(){
    int m[] = {3, 2, -6};
    int n[] = {2, -12, -3};

    write_data(m, n);

    double angle = acos(dot(m, n, 3)/(norm_square(m, 3), norm_square(n, 3)))*180/M_PI;
    printf("Angle between lines: %lf\n", angle);

    return 0;
}