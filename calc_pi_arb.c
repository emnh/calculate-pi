#include <stdio.h>
#include <mpfr.h>

void calculatePi(mpfr_t result, unsigned long int numRectangles) {
    mpfr_t width, x, height, sum;
    mpfr_inits2(256, width, x, height, sum, NULL);

    mpfr_set_ui(width, numRectangles, MPFR_RNDN);
    mpfr_ui_div(width, 1, width, MPFR_RNDN);

    mpfr_set_d(sum, 0.0, MPFR_RNDN);

    for (unsigned long int i = 0; i < numRectangles; ++i) {
        mpfr_set_ui(x, i, MPFR_RNDN);
        mpfr_add_d(x, x, 0.5, MPFR_RNDN);
        mpfr_mul(x, x, width, MPFR_RNDN);

        mpfr_mul(x, x, x, MPFR_RNDN);
        mpfr_add_ui(x, x, 1, MPFR_RNDN);
        mpfr_set_d(height, 4.0, MPFR_RNDN);
        mpfr_div(height, height, x, MPFR_RNDN);
//        mpfr_ui_div(height, 1, height, MPFR_RNDN);*/
/*        mpfr_add(height, height, x, MPFR_RNDN);*/
/*        mpfr_div(height, height, x, MPFR_RNDN);*/
/*        mpfr_ui_div(height, 1, height, MPFR_RNDN);*/

        mpfr_add(sum, sum, height, MPFR_RNDN);
    }

    mpfr_mul(result, width, sum, MPFR_RNDN);

    mpfr_clears(width, x, height, sum, NULL);
}

int main() {
    mpfr_t pi;
    mpfr_init2(pi, 256); // 256 bits precision

    unsigned long int numRectangles;

    // Input: Number of rectangles to use for Riemann sum
    printf("Enter the number of rectangles: ");
    scanf("%lu", &numRectangles);

    // Check for a valid input
    if (numRectangles <= 0) {
        printf("Please enter a positive integer for the number of rectangles.\n");
        mpfr_clear(pi);
        return 1;  // Exit with an error code
    }

    // Calculate Pi using Riemann integrals with arbitrary precision
    calculatePi(pi, numRectangles);

    // Output the result
    mpfr_printf("Approximation of Pi using %lu rectangles: %.40Rf\n", numRectangles, pi);

    mpfr_clear(pi);

    return 0;
}
