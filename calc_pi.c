#include <stdio.h>

double calculatePi(int numRectangles) {
    double width = 1.0 / numRectangles;
    double sum = 0.0;

    for (int i = 0; i < numRectangles; ++i) {
        double x = (i + 0.5) * width;
        double height = 4.0 / (1.0 + x * x);
        sum += height;
    }

    return width * sum;
}

int main() {
    int numRectangles;

    // Input: Number of rectangles to use for Riemann sum
    printf("Enter the number of rectangles: ");
    scanf("%d", &numRectangles);

    // Check for a valid input
    if (numRectangles <= 0) {
        printf("Please enter a positive integer for the number of rectangles.\n");
        return 1;  // Exit with an error code
    }

    // Calculate Pi using Riemann integrals
    double pi = calculatePi(numRectangles);

    // Output the result
    printf("Approximation of Pi using %d rectangles: %lf\n", numRectangles, pi);

    return 0;
}
