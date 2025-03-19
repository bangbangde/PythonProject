[Image](url)

SPECIFICATION

Revision: A07

Date：2024-03-01

Issued

Model No.:MP300S

Description: Consumption Open Frame

AC/DC Power Supply

| PREPAREDBY   | CHECKEDBY   | APPROVED BY   |
|:-------------|:------------|:--------------|
| WangXiaodong | LiXiaobing  | LiXiaobing    |

深圳麦格米特电气股份有限公司

SHENZHEN MEGMEET ELECTRICAL STOCK CO.,LTD

Add:5th Floor, Tower A, B,C501-C503,D,E, Unis Inforport,No.13 Langshan Road,

North Section, Hi-Tech Industrial Park, Nanshan District, Shenzhen, PEOPLE'S

REPUBLIC OF CHINA

Tel: +86 0755-8660 0500Fax: +86 0755-8660 0999

E-mail: megmeet@megmeet.com; http://www.megmeet.com

Specification Document No.：

[Image](url)

Model：MP300S Issued Date : 2024-03-01

Revision History

| Revision   | ChangeItem                                                      | Date       |
|:-----------|:----------------------------------------------------------------|:-----------|
| A00        | InitialRelease                                                  | 2020-12-09 |
| A01        | 1、1.1.5 Efficiency: Upto93%/95%Updateto91.5%/94%;              | 2021-01-20 |
|            | 2、1.3.1Overcurrentprotection: Mainoutput 105%~150%Updateto     |            |
|            | 120%~160%,5Vsb110%~150%Updateto120%~200%                        |            |
| A02        | 1、Increase15Voutputspecifications；                            | 2021-03-15 |
|            | 2、Updatemechanicaldimensiondrawing                             |            |
| A03        | 3、1、1.4.1PS_ON： Low(0~0.8V)=ON Upto                          | 2021-05-06 |
|            | Low(0~0.8V)orfloating=ON；                                      |            |
| A04        | 1、Update6.2Mechanicalspecification                             | 2022-04-14 |
| A05        | 2.2Dielectricstrength:OutputtoPE500Vac50Hz1minute ≤10mAUpdateto | 2023-02-16 |
|            | 1500Vac50Hz1minute ≤10mA;                                       |            |
| A06        | Update6.3.1Coolingconvection300W                                | 2023-03-02 |
| A07        | 1、Update 3.Safety；                                            | 2024-03-01 |
|            | 2、Update 4.EMC                                                 |            |

Page 2 of 11

The copyright belongs to Megmeet. Any unauthorized use is prohibited.

Specification Document No.：

[Image](url)

Model：MP300S Issued Date : 2024-03-01

Content

1. Electrical specification:.......................................................................................................................................4

1.1 Input electrical characteristics.................................................................................................................. 4

1.2 Output electrical characteristics................................................................................................................4

1.3 Protection..................................................................................................................................................5

1.4 Signals.......................................................................................................................................................5

2. Isolation...............................................................................................................................................................6

2.1 Insulation resistance..................................................................................................................................6

2.2 Dielectric strength.....................................................................................................................................6

3. Safety...................................................................................................................................................................6

4. EMC.................................................................................................................................................................6

4.1 EMI........................................................................................................................................................... 6

4.2 EMS...........................................................................................................................................................7

5. Reliability and environmental requirement.....................................................................................................7

5.1 Temperature...............................................................................................................................................7

5.2 Humidity................................................................................................................................................... 7

5.3Altitude......................................................................................................................................................7

5.4 Cooling method.........................................................................................................................................7

5.5 Vibration....................................................................................................................................................8

5.6 Shock.........................................................................................................................................................8

6. Dimension...........................................................................................................................................................8

6.1 PCB................................................................................................................................................................... 8

6.2 Mechanical specification.................................................................................................................................. 8

6.3 Derating curve.................................................................................................................................................10

7.Other characteristics...........................................................................................................................................11

7.1 MTBF......................................................................................................................................................11

7.2Weight...................................................................................................................................................... 11

Page 3 of 11

The copyright belongs to Megmeet. Any unauthorized use is prohibited.

Specification Document No.：

[Image](url)

Model：MP300S Issued Date : 2024-03-01

1. Electrical specification:

1.1 Input electrical characteristics

| No.    | Electrical characteristics      | MP300S                                |
|:-------|:--------------------------------|:--------------------------------------|
| 1.1.1  | Inputvoltagerang                | 85Vacto264Vac                         |
| 1.1.2  | Normalvoltage                   | 100～240Vac                           |
| 1.1.3  | Frequencyrange                  | 47Hz--63Hz                            |
| 1.1.4  | Maxinputaccurrent(100Vac)       | 3.5A                                  |
| 1.1.5  | Efficiency(115/230Vac,fullload) | 91.5%/94%                             |
|        | Typ                             |                                       |
| 1.1.6  | Powerfactor(100Vac~240Vac,      | 0.95                                  |
|        | fullload)                       |                                       |
| 1.1.7  | Inrushcurrent(240Vac)           | 50A                                   |
| 1.1.8  | Powersaving                     | 0.6W/230Vac(Remoteoffandnoloadon5Vsb) |
| 1.1.9  | Holduptime                      | >20ms300Wload                         |
| 1.1.10 | Earthleakagecurrent(NC/SFC)     | 0.15mA/0.3mA                          |
|        | Touchcurrent(NC/SFC)            | 0.1mA/0.2mA                           |
| 1.1.11 | Ratedoutputpower                | 300W@coolconvection                   |
| 1.1.12 | Inputfuse                       | T5A/250Vac                            |

1.2 Output electrical characteristics

| No.   | Electrical characteristics   | MP300S                                           | None   | None   | None   | None   | None   | None   |
|:------|:-----------------------------|:-------------------------------------------------|:-------|:-------|:-------|:-------|:-------|:-------|
| 1.2.1 | Mainoutputvoltage            | 12V                                              | 15V    | 19V    | 24V    | 28V    | 36V    | 48V    |
| 1.2.2 | Outputcurrent                | 25.0A                                            | 20.0A  | 15.8A  | 12.5A  | 10.8A  | 8.33A  | 6.25A  |
| 1.2.3 | Voltageregulation            | line regulation: ±0.5%;                          |        |        |        |        |        |        |
|       |                              | load regulation:±2%；                            |        |        |        |        |        |        |
|       |                              | voltage regulation accuracy±2%                   |        |        |        |        |        |        |
| 1.2.4 | Outputripple&noise.          | 12V-15V:200mV,19V-28V:280mV,32V-48V:480mV        |        |        |        |        |        |        |
| 1.2.5 | Outputtransientresponse.     | ±5%ofoutputvoltage；stepload： 5%-50%or50-100%， |        |        |        |        |        |        |
|       |                              | slewrate1A/us                                    |        |        |        |        |        |        |

Page 4 of 11

The copyright belongs to Megmeet. Any unauthorized use is prohibited.

Specification Document No.：

[Image](url)

Model：MP300S Issued Date : 2024-03-01

| 1.2.6   | Startuptime           | ≤2.0s@100Vacinput,25℃；   |
|:--------|:----------------------|:--------------------------|
| 1.2.7   | Outputovershootduring | 5%                        |
|         | turn-on&turn-off      |                           |
| 1.2.8   | Outputvoltagerisetime | 5<Tr≤100ms                |

| No.    | Electrical characteristics   | MP300S                         |
|:-------|:-----------------------------|:-------------------------------|
| 1.2.9  | Standbyoutputvoltage         | 5V                             |
| 1.2.10 | Outputcurrent                | 2A                             |
| 1.2.11 | Voltageregulation            | line regulation: ±0.5%;        |
|        |                              | load regulation:±2%；          |
|        |                              | voltage regulation accuracy±5% |
| 1.2.12 | Outputripple&noise.          | 2%                             |

1.3 Protection

| No.   | Protection item           | MP300S               | None     | None                 | None              |
|:------|:--------------------------|:---------------------|:---------|:---------------------|:------------------|
|       |                           | Main output          |          | 5Vsb                 |                   |
| 1.3.1 | Overcurrentprotection     | 120%~160%            |          | 120%~200%            |                   |
|       |                           | hiccup，autorecovery |          | hiccup，autorecovery |                   |
| 1.3.2 | Shortcircuitprotection    | hiccup，autorecovery |          | hiccup，autorecovery |                   |
| 1.3.3 | Outputvoltageprotection   | 110%~150%            |          | /                    |                   |
|       |                           | latchoff             |          | /                    |                   |
| 1.3.4 | Inputbrownin/out          | brownin              | brownout |                      | minimumhysteresis |
|       |                           | <=85Vac              | >=60Vac  |                      | 5Vac              |
| 1.3.5 | Overtemperatureprotection | autorecovery         |          |                      |                   |

1.4 Signals

Page 5 of 11

The copyright belongs to Megmeet. Any unauthorized use is prohibited.

Specification Document No.：

[Image](url)

Model：MP300S Issued Date : 2024-03-01

| No.   | Electrical Characteristics   | MP300S                                  |
|:------|:-----------------------------|:----------------------------------------|
| 1.4.1 | PS_ON                        | Low(0~0.8V)orfloating=ON,High(3~5V)=OFF |
| 1.4.2 | 5VFAN                        | Fanpowered                              |
| 1.4.3 | Powergood                    | CombinedACFailandDCOKsignal             |
|       |                              | Low(0~0.8V)=Fail,High(3~5.5V)=OK        |

2. Isolation

2.1 Insulation resistance

| Input toOutput   | DC500V10MΩ.             |
|                  | (at room temperature)   |
|:-----------------|:------------------------|
| Input toPE       | DC500V10MΩ.             |
|                  | (at room temperature)   |
| Output toPE      | DC500V10MΩ.             |
|                  | (at room temperature)   |

(at room temperature)

2.2 Dielectric strength

| Input toOutput   | 4000Vac50Hz1minute≤10mA   |
|:-----------------|:--------------------------|
| Input to PE      | 1500Vac50Hz1minute≤10mA   |
| Output to PE     | 1500Vac50Hz 1minute≤10mA  |

3. Safety

* IEC 60601-1，IEC 62368-1

* ANSI/AAMI ES 60601-1

* CSA C22.2 No. 60601-1

* Protection type: Class I

4. EMC

4.1 EMI

The power supply shall comply with the following criterion:

1) Conduction Emission :

* CISPR 11, CLASS B

2) Radiated Emission :

Page 6 of 11

The copyright belongs to Megmeet. Any unauthorized use is prohibited.

Specification Document No.：

[Image](url)

Model：MP300S Issued Date : 2024-03-01

* CISPR 11, CLASS B

3) Voltage Fluctuation & Flicker :

* IEC 61000-3-3 Class A

Distortion）:

4) Harmonic

* IEC 61000-3-2 Class A

4.2 EMS

The power supply shall comply with the following criterion:

ESD：IEC 61000-4-2 Class A

1)

8KV contact discharges & 15KV air discharges

EFT：IEC 61000-4-4 Class A

2)

Power supply lines: ±2kV

SURGE：IEC 61000-4-5Class A

3)

Line to line: ±1kV, line to earth: ±2kV, 12 ohms

DIP：IEC 61000-4-11 Criterion A/B/C

4)

| Drop   | Time   | Standard   |
|:-------|:-------|:-----------|
| 0％Ut  | 10ms   | A          |
| 0％Ut  | 20ms   | B          |
| 70%Ut  | 500ms  | B          |
| 0%Ut   | 5000ms | B          |

Immunity：IEC 61000-4-6 Class A

5) Conducted

Immunity：IEC 61000-4-3 Class A

6) Radiated

Fields：IEC 61000-4-8 Class A

7) Magnetic

5. Reliability and environmental requirement

5.1 Temperature

* Operating temperature : -10℃ to +70℃, See the derating curve below.

* Storage temperature : -40℃ to +80℃.

5.2 Humidity

* Operating: From 5% to 95% relative humidity (non-condensing).

* Storage: From 5% to 100% relative humidity (non-condensing).

5.3 Altitude

* Operating: -60 to 5000 m

* Storage: up to 5000 m

5.4 Cooling method

* Cooling convection 300 W.

Page 7 of 11

The copyright belongs to Megmeet. Any unauthorized use is prohibited.

Specification Document No.：

[Image](url)

Model：MP300S Issued Date : 2024-03-01

5.5 Vibration

* 10-500Hz, 19.6m/s² (2G), 30minutes each along X, Y and Z axis.

5.6 Shock

* 98m/s² (10G), 6ms, once each X, Y and Z axis.

6. Dimension

6.1 PCB

*Length*Width*High：127mm*76.2mm*38mm

6.2 Mechanical specification

6.2.1 Open Frame Unit

[Image](url)

Page 8 of 11

The copyright belongs to Megmeet. Any unauthorized use is prohibited.

Specification Document No.：

[Image](url)

Model：MP300S Issued Date : 2024-03-01

[Image](url)

|       |   PIN | None   | Terminalmodel               | Matchingterminals   |
|       |       |        |                             | andplasticshell     |
|:------|------:|:-------|:----------------------------|:--------------------|
| CN100 |     1 | PE     | VH-5ADW3(华富(嘉得电子))    | 华富：VH-5Y         |
|       |       |        | （Orequivalent）            | 华富：VH            |
|       |       |        |                             | （Orequivalent）    |
|       |     3 | N      |                             |                     |
|       |     5 | L      |                             |                     |
| CN201 |     1 | VOUT+  | M4OUTPUTTERMINAL            |                     |
| CN202 |     1 | VOUT-  | M4OUTPUTTERMINAL            |                     |
| CN200 |     1 | PS_ON  | 胜蓝                        | 胜蓝：              |
|       |       |        | (12002W00-2X3P-L-S1-23-HF)/ | 12002H00-2X3P-L     |
|       |       |        | 加炜                        | 胜蓝：12002T0P-2E   |
|       |       |        | (A2006WV-2x3P-6T2-5eHK2.3)  | （Orequivalent）    |
|       |       |        | （Orequivalent）            |                     |
|       |     2 | Power  |                             |                     |
|       |       | Good   |                             |                     |
|       |     3 | DGND   |                             |                     |
|       |     4 | NC     |                             |                     |
|       |     5 | DGND   |                             |                     |
|       |     6 | 5Vsb   |                             |                     |
| CN203 |     1 | DGND   | XH-2A(华富(嘉得电子))       | 华富：XH-2Y         |
|       |       |        | （Orequivalent）            | 华富：XH            |
|       |       |        |                             | （Orequivalent）    |
|       |     2 | 5Vsb   |                             |                     |

Page 9 of 11

The copyright belongs to Megmeet. Any unauthorized use is prohibited.

Specification Document No.：

[Image](url)

Model：MP300S Issued Date : 2024-03-01

6.3 Derating curve

6.3.1 Cooling convection 300 W

Derating versus Input Voltage:

[Image](url)

Derating and ambient temperature:

Page 10 of 11

The copyright belongs to Megmeet. Any unauthorized use is prohibited.

Specification Document No.：

[Image](url)

Model：MP300S Issued Date : 2024-03-01

[Image](url)

7.Other characteristics

7.1 MTBF

* >100,000 Hour, @230Vac, 25℃, Rated output

7.2Weight

* ＜ 550 g

Page 11 of 11

The copyright belongs to Megmeet. Any unauthorized use is prohibited.