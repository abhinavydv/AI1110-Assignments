#include <stdio.h>
#include <math.h>
#include <stdbool.h>


#define NUM_POINTS 1000


/*
Stores roots of the equation in root1 and root2.
Returns true if root are real else false.
*/
bool quadratic_roots(double a, double b, double c, double *root1, double *root2){
    double d = b*b - 4*a*c;

    if (d<0)
        return false;

    *root1 = (-b+sqrt(d))/(2*a);
    *root2 = (-b-sqrt(d))/(2*a);

    return true;
}


// write points to be plotted to a file. First line contains roots of equation
void write_points(double a, double b, double c, double root1, double root2){
    FILE *f = fopen("data.txt", "w");

    double min, max;

    if (root1<root2){
        min = root1;
        max = root2;
    }
    else{
        min = root2;
        max = root1;
    }

    
    double x, y, diff;

    min *= 1.2;
    max *= 1.2;

    diff = max-min;

    fprintf(f, "%lf %lf\n", root1, root2);
    

    for (int i=0; i<NUM_POINTS; i++){
        x = min + i*diff/NUM_POINTS;
        y = a*x*x + b*x + c;
        fprintf(f, "%lf %lf\n", x, y);
    }

    fclose(f);
}


/*
Stores the consecutive numbers which are multiples of `multiple_of`
and whose product is `product` in num1 and num2.
Returns true if numbers exist else false.
*/
bool find_cons_num(int product, int multiple_of, int *num1, int *num2){

    double a, b, c, root1, root2;

    // Equation :  multiple_of^2*x^2 + multiple_of^2*x - product = 0
    a = b = pow(multiple_of, 2);
    c = -product;

    bool check = quadratic_roots(a, b, c, &root1, &root2);

    write_points(a, b, c, root1, root2);

    if (!check)
        return false;

    if (root1 > 0)
        *num1 = multiple_of * (int)root1;
    else
        *num1 = multiple_of * (int)root2;

    *num2 = *num1 + multiple_of;

    int n1, n2;
    n1 = *num1;
    n2 = *num2;

    if (n1>0 && n2>0 && n1*n2 == product && n1%multiple_of==0 && n2%multiple_of==0)
        return true;
    return false;
}


int main(){
    int product, multiple_of, num1, num2;

    product = 810;
    multiple_of = 3;

    bool check = find_cons_num(product, multiple_of, &num1, &num2);

    if (!check)
        printf("No such numbers found.\n");
    else
        printf("The numbers are: \n%d %d\n", num1, num2);

    return 0;
}