#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int main(void) // main function begins
{

    // Uniform random numbers
    // uniform("uni.dat", 1000000);

    // Gaussian random numbers
    //  gaussian("gau.dat", 1000000);

    // generate X
    // x_gen("gau.dat", 1000000);

    // generate V
    // v_gen("ln.dat", 1000000);

    // Mean of uniform
    // printf("uni mean: %lf\n", mean("uni.dat"));
    // printf("uni var: %lf\n", var("uni.dat"));
    printf("gau mean: %lf\n", mean("gau.dat"));
    printf("gau var: %lf\n", var("gau.dat"));
    // printf("ln mean: %lf\n", mean("ln.dat"));
    // printf("ln var: %lf\n", var("ln.dat"));
    return 0;
}
