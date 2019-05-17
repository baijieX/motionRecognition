#include "example.h"
#include <iostream>
#include <float.h>
#include <complex>
#include <cmath>
#include <string.h>
#include <errno.h>

#define F 1.0e+6
#define V 10
#define ZR 5
#define ZT 5
#define TX_R 0.1 
#define HEIGHT 0.05

using namespace std;

void example7(){
    double w = 2*PI*F;

	GlobalCoupler* GC = GlobalCoupler::getInstance(4, DEFAULT_PERMEABILITY, F);

	complexDouble srcV;
	srcV.real = V;
	srcV.imag = 0.0;
	complexDouble dstV;
	dstV.real = 0.0;
	dstV.imag = 0.0;

	Resonator* TX1 = new Resonator(new Coil(), ZT, srcV);
	Resonator* TX2 = new Resonator(new Coil(), ZT, srcV);
	Resonator* TX3 = new Resonator(new Coil(), ZT, srcV);
	Resonator* RX = new Resonator(new Coil(), ZR, dstV);

	TX1->translateCoil(-TX_R, -TX_R*tan(PI/6), 0.0);
	TX2->translateCoil(TX_R, -TX_R*tan(PI/6), 0.0);
	TX3->translateCoil(0.0, TX_R/cos(PI/6), 0.0);
	RX->translateCoil(0, 0, HEIGHT);//初始RX开路



	double x=0, y=0, oldX, oldY;
	int numTrace=0;
	FILE *inF;//输入文件,坐标
	FILE *outF;//输出文件,互感
	outF = fopen("tmpData.csv","w");
	if (outF == NULL) {
		cout<<"Failed to train.csv"<<endl;
		exit(1);
	}
	fprintf(outF, "tag,");
	int numM=30;
	while (numM--){
		fprintf(outF, "M%d,", 30-numM);
	}
	fseek(outF, -1, SEEK_CUR);
	fprintf(outF, "\n");

	for (int i=0;i<4;i++){//i=0,1,2,3代表上下左右4个输入文件
		char fileName[15];
		switch (i){
			case 0: strcpy(fileName, "up.txt");break;
			case 1: strcpy(fileName, "down.txt");break;
			case 2: strcpy(fileName, "left.txt");break;
			case 3: strcpy(fileName, "right.txt");break;
			default: cout<<"Error"<<endl;exit(1);
		}
		inF = fopen(fileName, "r");
		if (inF == NULL) {
			cout<<"Failed to open "<<fileName<<" errno="<<errno<<": "<<strerror(errno)<<endl;
			exit(1);
		}
		while (!feof(inF)){//每次循环一个轨迹,10个点
			fprintf(outF, "%d,", i);
			int numDot=10;
			while (numDot--){//每次循环一个点，坐标-》M
				oldX=x;	oldY=y;
				fscanf(inF,"%lf,%lf\n", &x, &y);
				x = (x-250)/250*TX_R; 
				y = (y-250)/250*TX_R; 
				RX->translateCoil(x-oldX, y-oldY, 0);
				//cout<<numDot<<endl;
				GC->updateRXMutualInductances();
				//cout<<numDot<<endl;
				fprintf(outF, "%lf,%lf,%lf,", (*GC->partialZMatrix)(1,4),
											  (*GC->partialZMatrix)(2,4),
											  (*GC->partialZMatrix)(3,4) );
		//						fclose(outF);fclose(inF);
		//						return;

			}
				cout<<numTrace++<<endl;//////////
			fseek(outF, -1, SEEK_CUR);
			fprintf(outF, "\n");
			fscanf(inF, "\n");
		}
		fclose(inF);
	}
	fclose(outF);



    delete TX1;
    delete TX2;
    delete TX3;
	delete RX;
	GC->destroyEnvironment();
    return;

}

