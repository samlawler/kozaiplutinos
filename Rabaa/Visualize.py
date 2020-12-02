import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme(style="darkgrid")





#for file in range(2, 10):
Index0, SMA0, Ecc0, Inc0, Node0, ArgPeri0, MeanAnom0, Name0, AverageSMA0, AverageEcc0, AverageInc0, LibrationCenter0, LibrationAmp0, KozaiCenter0, KozaiAmp0= np.genfromtxt(
             "TPCheck1.out", unpack=True)
Index2, SMA2, Ecc2, Inc2, Node2, ArgPeri2, MeanAnom2, Name2, AverageSMA2, AverageEcc2, AverageInc2, LibrationCenter2, LibrationAmp2, KozaiCenter2, KozaiAmp2= np.genfromtxt(
             "TPCheck2.out", unpack=True)
Index3, SMA3, Ecc3, Inc3, Node3, ArgPeri3, MeanAnom3, Name3, AverageSMA3, AverageEcc3, AverageInc3, LibrationCenter3, LibrationAmp3, KozaiCenter3, KozaiAmp3= np.genfromtxt(
             "TPCheck3.out", unpack=True)
Index4, SMA4, Ecc4, Inc4, Node4, ArgPeri4, MeanAnom4, Name4, AverageSMA4, AverageEcc4, AverageInc4, LibrationCenter4, LibrationAmp4, KozaiCenter4, KozaiAmp4= np.genfromtxt(
             "TPCheck4.out", unpack=True)
Index5, SMA5, Ecc5, Inc5, Node5, ArgPeri5, MeanAnom5, Name5, AverageSMA5, AverageEcc5, AverageInc5, LibrationCenter5, LibrationAmp5, KozaiCenter5, KozaiAmp5= np.genfromtxt(
             "TPCheck5.out", unpack=True)
Index6, SMA6, Ecc6, Inc6, Node6, ArgPeri6, MeanAnom6, Name6, AverageSMA6, AverageEcc6, AverageInc6, LibrationCenter6, LibrationAmp6, KozaiCenter6, KozaiAmp6= np.genfromtxt(
             "TPCheck6.out", unpack=True)
Index7, SMA7, Ecc7, Inc7, Node7, ArgPeri7, MeanAnom7, Name7, AverageSMA7, AverageEcc7, AverageInc7, LibrationCenter7, LibrationAmp7, KozaiCenter7, KozaiAmp7= np.genfromtxt(
             "TPCheck7.out", unpack=True)
Index8, SMA8, Ecc8, Inc8, Node8, ArgPeri8, MeanAnom8, Name8, AverageSMA8, AverageEcc8, AverageInc8, LibrationCenter8, LibrationAmp8, KozaiCenter8, KozaiAmp8= np.genfromtxt(
             "TPCheck8.out", unpack=True)
Index9, SMA9, Ecc9, Inc9, Node9, ArgPeri9, MeanAnom9, Name9, AverageSMA9, AverageEcc9, AverageInc9, LibrationCenter9, LibrationAmp9, KozaiCenter9, KozaiAmp9= np.genfromtxt(
             "TPCheck9.out", unpack=True)
Index10, SMA10, Ecc10, Inc10, Node10, ArgPeri10, MeanAnom10, Name10, AverageSMA10, AverageEcc10, AverageInc10, LibrationCenter10, LibrationAmp10, KozaiCenter10, KozaiAmp10= np.genfromtxt(
             "TPCheck9.out", unpack=True)

Indexp1 = np.append(Index2, Index0)
Indexp2 = np.append(Indexp1, Index3)
Indexp3 = np.append(Indexp2, Index4)
Indexp4 = np.append(Indexp3, Index5)
Indexp5 = np.append(Indexp4, Index6)
Indexp6 = np.append(Indexp5, Index7)
Indexp7= np.append(Indexp6, Index8)
Indexp8= np.append(Indexp7, Index9)
IndexpFinal= np.append(Indexp8, Index10)

SMAp1 = np.append(SMA0, SMA2)
SMAp2 = np.append(SMAp1, SMA3)
SMAp3 = np.append(SMAp2, SMA4)
SMAp4 = np.append(SMAp3, SMA5)
SMAp5 = np.append(SMAp4, SMA6)
SMAp6 = np.append(SMAp5, SMA7)
SMAp7= np.append(SMAp6, SMA8)
SMAp8= np.append(SMAp7, SMA9)
SMApFinal= np.append(SMAp8, SMA10)

Eccp1 = np.append(Ecc2, Ecc0)
Eccp2 = np.append(Eccp1, Ecc3)
Eccp3 = np.append(Eccp2, Ecc4)
Eccp4 = np.append(Eccp3, Ecc5)
Eccp5 = np.append(Eccp4, Ecc6)
Eccp6 = np.append(Eccp5, Ecc7)
Eccp7 = np.append(Eccp6, Ecc8)
Eccp8 = np.append(Eccp7, Ecc9)
EccpFinal = np.append(Eccp8, Ecc10)

Incp1 = np.append(Inc2, Inc0)
Incp2 = np.append(Incp1, Inc3)
Incp3 = np.append(Incp2, Inc4)
Incp4 = np.append(Incp3, Inc5)
Incp5 = np.append(Incp4, Inc6)
Incp6 = np.append(Incp5, Inc7)
Incp7 = np.append(Incp6, Inc8)
Incp8 = np.append(Incp7, Inc9)
IncpFinal = np.append(Incp8, Inc10)

Nodep1 = np.append(Node2, Node0)
Nodep2 = np.append(Nodep1, Node3)
Nodep3 = np.append(Nodep2, Node4)
Nodep4 = np.append(Nodep3, Node5)
Nodep5 = np.append(Nodep4, Node6)
Nodep6 = np.append(Nodep5, Node7)
Nodep7 = np.append(Nodep6, Node8)
Nodep8 = np.append(Nodep7, Node9)
NodepFinal = np.append(Nodep8, Node10)

ArgPerip1 = np.append(ArgPeri2, ArgPeri0)
ArgPerip2 = np.append(ArgPerip1, ArgPeri3)
ArgPerip3 = np.append(ArgPerip2, ArgPeri4)
ArgPerip4 = np.append(ArgPerip3, ArgPeri5)
ArgPerip5 = np.append(ArgPerip4, ArgPeri6)
ArgPerip6 = np.append(ArgPerip5, ArgPeri7)
ArgPerip7 = np.append(ArgPerip6, ArgPeri8)
ArgPerip8 = np.append(ArgPerip7, ArgPeri9)
ArgPeripFinal = np.append(ArgPerip8, ArgPeri10)

MeanAnomp1 = np.append(MeanAnom2, MeanAnom0)
MeanAnomp2 = np.append(MeanAnomp1, MeanAnom3)
MeanAnomp3 = np.append(MeanAnomp2, MeanAnom4)
MeanAnomp4 = np.append(MeanAnomp3, MeanAnom5)
MeanAnomp5 = np.append(MeanAnomp4, MeanAnom6)
MeanAnomp6 = np.append(MeanAnomp5, MeanAnom7)
MeanAnomp7 = np.append(MeanAnomp6, MeanAnom8)
MeanAnomp8 = np.append(MeanAnomp7, MeanAnom9)
MeanAnompFinal = np.append(MeanAnomp8, MeanAnom10)

Namep1 = np.append(Name2, Name0)
Namep2 = np.append(Namep1, Name3)
Namep3 = np.append(Namep2, Name4)
Namep4 = np.append(Namep3, Name5)
Namep5 = np.append(Namep4, Name6)
Namep6 = np.append(Namep5, Name7)
Namep7 = np.append(Namep6, Name8)
Namep8 = np.append(Namep7, Name9)
#NamepFinal = np.append(Namep8, Name10)

AverageSMAp1 = np.append(AverageSMA2, AverageSMA0)
AverageSMAp2 = np.append(AverageSMAp1, AverageSMA3)
AverageSMAp3 = np.append(AverageSMAp2, AverageSMA4)
AverageSMAp4 = np.append(AverageSMAp3, AverageSMA5)
AverageSMAp5 = np.append(AverageSMAp4, AverageSMA6)
AverageSMAp6 = np.append(AverageSMAp5, AverageSMA7)
AverageSMAp7 = np.append(AverageSMAp6, AverageSMA8)
AverageSMAp8 = np.append(AverageSMAp7, AverageSMA9)
AverageSMApFinal = np.append(AverageSMAp8, AverageSMA10)

AverageEccp1 = np.append(AverageEcc2, AverageEcc0)
AverageEccp2 = np.append(AverageEccp1, AverageEcc3)
AverageEccp3 = np.append(AverageEccp2, AverageEcc4)
AverageEccp4 = np.append(AverageEccp3, AverageEcc5)
AverageEccp5 = np.append(AverageEccp4, AverageEcc6)
AverageEccp6 = np.append(AverageEccp5, AverageEcc7)
AverageEccp7 = np.append(AverageEccp6, AverageEcc8)
AverageEccp8 = np.append(AverageEccp7, AverageEcc9)
AverageEccpFinal = np.append(AverageEccp8, AverageEcc10)

AverageIncp1 = np.append(AverageInc2, AverageInc0)
AverageIncp2 = np.append(AverageIncp1, AverageInc3)
AverageIncp3 = np.append(AverageIncp2, AverageInc4)
AverageIncp4 = np.append(AverageIncp3, AverageInc5)
AverageIncp5 = np.append(AverageIncp4, AverageInc6)
AverageIncp6 = np.append(AverageIncp5, AverageInc7)
AverageIncp7 = np.append(AverageIncp6, AverageInc8)
AverageIncp8 = np.append(AverageIncp7, AverageInc9)
AverageIncpFinal = np.append(AverageIncp8, AverageInc10)

LibrationCenterp1 = np.append(LibrationCenter2, LibrationCenter0)
LibrationCenterp2 = np.append(LibrationCenterp1, LibrationCenter3)
LibrationCenterp3 = np.append(LibrationCenterp2, LibrationCenter4)
LibrationCenterp4 = np.append(LibrationCenterp3, LibrationCenter5)
LibrationCenterp5 = np.append(LibrationCenterp4, LibrationCenter6)
LibrationCenterp6 = np.append(LibrationCenterp5, LibrationCenter7)
LibrationCenterp7 = np.append(LibrationCenterp6, LibrationCenter8)
LibrationCenterp8 = np.append(LibrationCenterp7, LibrationCenter9)
LibrationCenterpFinal = np.append(LibrationCenterp8, LibrationCenter10)

LibrationAmpp1 = np.append(LibrationAmp2, LibrationAmp0)
LibrationAmpp2 = np.append(LibrationAmpp1, LibrationAmp3)
LibrationAmpp3 = np.append(LibrationAmpp2, LibrationAmp4)
LibrationAmpp4 = np.append(LibrationAmpp3, LibrationAmp5)
LibrationAmpp5 = np.append(LibrationAmpp4, LibrationAmp6)
LibrationAmpp6 = np.append(LibrationAmpp5, LibrationAmp7)
LibrationAmpp7 = np.append(LibrationAmpp6, LibrationAmp8)
LibrationAmpp8 = np.append(LibrationAmpp7, LibrationAmp9)
LibrationAmppFinal = np.append(LibrationAmpp8, LibrationAmp10)

KozaiCenterp1 = np.append(KozaiCenter2, KozaiCenter0)
KozaiCenterp2 = np.append(KozaiCenterp1, KozaiCenter3)
KozaiCenterp3 = np.append(KozaiCenterp2, KozaiCenter4)
KozaiCenterp4 = np.append(KozaiCenterp3, KozaiCenter5)
KozaiCenterp5 = np.append(KozaiCenterp4, KozaiCenter6)
KozaiCenterp6 = np.append(KozaiCenterp5, KozaiCenter7)
KozaiCenterp7 = np.append(KozaiCenterp6, KozaiCenter8)
KozaiCenterp8 = np.append(KozaiCenterp7, KozaiCenter9)
KozaiCenterpFinal = np.append(KozaiCenterp8, KozaiCenter10)


with open("TPCheck1.out") as f:  # Counting number of lines
    for line, l in enumerate(f):
        pass
NumberOfLines = line * 9

i = 0

IsItKozai = np.zeros(len(IndexpFinal)) + 1
for i in range(0, len(IndexpFinal)):
    if (LibrationCenterpFinal[i] == -999) | (LibrationCenterpFinal[i] == 0):
        LibrationCenterpFinal[i] = False
        IsItKozai[i] = 0
    else:
        LibrationCenterpFinal[i] = True
        IsItKozai[i] = 1
    if (KozaiCenterpFinal[i] == -999) | (KozaiCenterpFinal[i] == 0):
        KozaiCenterpFinal[i] = False
    else:
        KozaiCenterpFinal[i] = True
        IsItKozai[i] = 2





print(len(IndexpFinal))
sns.set_style('dark')
palette = sns.color_palette("mako", as_cmap=True)
sns.set_palette("dark", 10)
sns.relplot(x=SMApFinal, y=EccpFinal, hue=IsItKozai, style=IsItKozai, size=IsItKozai, sizes=(40,10))
plt.show()
