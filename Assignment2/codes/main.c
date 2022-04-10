#include <stdio.h>
#include <math.h>


#define NUM_POINTS 1000


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

    return 0;
}