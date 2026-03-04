#include <stdint.h>
#include <stdio.h>
#include <math.h>


void calculateSide(float a,float b, float c, char side) {
	switch (side) {
		
		case 'L': //Long side (hypotenuse)

			if ( !(a==0 || b==0) ) {
				float cSquared = (a*a) + (b*b); //Return C squared

				printf("%f", sqrt(cSquared));
				break;

			} else {
					printf("Please make sure the sides arent 0!\n");
					break;
			}

		case 'S': //Short side (adjacent or oppisite)

				if ( !(c==0 || b==0) ) {
					float aSquared = (c*c) - (b*b);

					printf("%f", sqrt(aSquared));
					break;

				} else {
						printf("Please make sure the sides arent 0!\n");
						break;
				}

		default:
			printf("Input a side! (L for hypotenuse and S for short side)\n");

	}
}

int main() {// 	 A B C Side 
	 calculateSide(0,5,0,'a');
}
