#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp;
    unsigned char imagem[512][512];
    int l,c; /* linha e coluna */
    if((fp = fopen("lena.bmp","rw")) == NULL) {
        printf("Impossivel de abrir o arquivo.\n");
        getchar();
        exit(1);
    } else {
        for(l=0;l<512;l++) {
            for(c=0;c<512;c++) {
                imagem[l][c]=(unsigned char) fgetc (fp);
            }
        }
        fclose(fp);
    }
    for(l=0;l<512;l++) {
        for(c=0;c<512;c++) {
            printf("%d ",imagem[l][c]);
            return 0;
        }
        printf("\n");
    }
    getchar();
    return(0);
}
