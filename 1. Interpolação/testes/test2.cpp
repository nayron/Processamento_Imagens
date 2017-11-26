#include <iostream>
#include <stdio.h>
#include <stdlib.h>

unsigned char* readBMP(char*);

int main() {
    readBMP("lena.bmp");
    return 0;
}

unsigned char* readBMP(char* filename) {
    int i;
    FILE* f = fopen(filename, "rb");
    unsigned char info[54];
    fread(info, sizeof(unsigned char), 54, f); // read the 54-byte header

    // extract image height and width from header
    int width = *(int*)&info[18];
    int height = *(int*)&info[22];

    int size = 3 * width * height;
    unsigned char* data = new unsigned char[size]; // allocate 3 bytes per pixel
    fread(data, sizeof(unsigned char), size, f); // read the rest of the data at once
    fclose(f);
    unsigned char* dataGrayScale = new unsigned char[width*height];
    int counter = 0;

    for(i = 0; i < size; i += 3) {
        dataGrayScale[i] = (data[i]+data[i+1]+data[i+2])/3; //the avg of the rgb is the grayscale value
        counter++;
    }

    delete [] data;  
    return dataGrayScale;
}
