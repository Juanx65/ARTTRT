# mobilenet bs 1
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  228,1  +23,2 -27,4 |   4.4 / 12.7    +0.5 -0.5 |  13.6      | 72.01                | 90.62               | 104     | 3487816    |
| TRT_fp32        |  906,8  +94,8 -112,6 |   1.1 / 2.4     +0.1 -0.1 |  14.0      | 72.01                | 90.62               | 88      | 3469760    |
| TRT_fp16        |  1.106,6  +112,1 -132,2 |   0.9 / 3.1     +0.1 -0.1 |  10.3      | 71.99                | 90.62               | 57      | 3469760    |
| TRT_int8        |  1.221,5  +130,2 -155,2 |   0.8 / 2.6     +0.1 -0.1 |  5.7       | 71.44                | 90.34               | 57      | 3469760    |
 
# mobilenet bs 32
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  966,0  +40,2 -42,8 |  33.1 / 36.7    +1.4 -1.4 |  13.6      | 72.02                | 90.63               | 109     | 3487816    |
| TRT_fp32        |  1.909,4  +212,0 -254,5 |  16.8 / 22.4    +2.1 -2.0 |  13.9      | 72.02                | 90.63               | 69      | 3469760    |
| TRT_fp16        |  2.794,6  +292,8 -347,7 |  11.5 / 16.1    +1.3 -1.3 |  9.0       | 72.01                | 90.64               | 58      | 3469760    |
| TRT_int8        |  3.511,9  +437,8 -539,0 |   9.1 / 13.3    +1.3 -1.2 |  4.6       | 71.44                | 90.31               | 57      | 3469760    |
 
# mobilenet bs 64
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  988,4  +27,8 -29,0 |  64.7 / 69.3    +1.9 -1.8 |  13.6      | 72.02                | 90.63               | 109     | 3487816    |
| TRT_fp32        |  2.021,7  +160,8 -182,7 |  31.7 / 36.5    +2.7 -2.6 |  13.9      | 72.02                | 90.63               | 69      | 3469760    |
| TRT_fp16        |  2.919,9  +295,6 -348,8 |  21.9 / 28.6    +2.5 -2.3 |  9.0       | 72.01                | 90.64               | 58      | 3469760    |
| TRT_int8        |  3.768,0  +440,1 -534,1 |  17.0 / 23.3    +2.2 -2.1 |  4.6       | 71.44                | 90.31               | 57      | 3469760    |
 
# mobilenet bs 128
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  997,7  +26,7 -27,8 | 128.3 / 135.8   +3.5 -3.5 |  13.6      | 72.05                | 90.64               | 109     | 3487816    |
| TRT_fp32        |  2.065,9  +137,7 -153,1 |  62.0 / 68.2    +4.4 -4.3 |  13.9      | 72.05                | 90.64               | 69      | 3469760    |
| TRT_fp16        |  3.322,3  +467,8 -593,6 |  38.5 / 48.0    +6.3 -5.8 |  9.0       | 72.05                | 90.65               | 58      | 3469760    |
| TRT_int8        |  3.818,4  +526,1 -663,8 |  33.5 / 42.9    +5.4 -5.0 |  4.6       | 71.47                | 90.32               | 57      | 3469760    |
 
# mobilenet bs 256
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  993,6  +26,2 -27,3 | 257.7 / 267.9   +7.0 -6.9 |  13.6      | 72.05                | 90.64               | 109     | 3487816    |
| TRT_fp32        |  1.892,5  +103,7 -113,1 | 135.3 / 147.5   +7.8 -7.6 |  13.9      | 72.05                | 90.64               | 69      | 3469760    |
| TRT_fp16        |  3.463,7  +331,7 -387,7 |  73.9 / 87.6    +7.8 -7.4 |  9.0       | 72.05                | 90.65               | 58      | 3469760    |
| TRT_int8        |  4.389,1  +546,3 -672,3 |  58.3 / 70.2    +8.3 -7.7 |  4.6       | 71.47                | 90.32               | 57      | 3469760    |
 
# resnet18 bs 1
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  367,6  +38,4 -45,5 |   2.7 / 6.5     +0.3 -0.3 |  44.7      | 69.76                | 89.08               | 53      | 11684712   |
| TRT_fp32        |  645,2  +36,7 -40,2 |   1.5 / 2.9     +0.1 -0.1 |  65.8      | 69.76                | 89.08               | 35      | 11678912   |
| TRT_fp16        |  961,5  +105,6 -126,5 |   1.0 / 3.2     +0.1 -0.1 |  24.9      | 69.76                | 89.09               | 27      | 11678912   |
| TRT_int8        |  1.136,1  +130,3 -157,6 |   0.9 / 1.9     +0.1 -0.1 |  13.3      | 69.57                | 88.94               | 25      | 11669504   |
 
# resnet18 bs 32
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  1.066,0  +59,2 -64,6 |  30.0 / 34.4    +1.8 -1.7 |  44.7      | 69.76                | 89.09               | 58      | 11684712   |
| TRT_fp32        |  1.093,0  +158,7 -203,1 |  29.3 / 34.7    +5.0 -4.6 |  51.7      | 69.76                | 89.09               | 30      | 11678912   |
| TRT_fp16        |  2.473,7  +215,0 -247,4 |  12.9 / 16.9    +1.2 -1.2 |  22.8      | 69.76                | 89.10               | 27      | 11678912   |
| TRT_int8        |  3.645,1  +466,2 -577,4 |   8.8 / 12.7    +1.3 -1.2 |  11.7      | 69.53                | 88.96               | 25      | 11669504   |
 
# resnet18 bs 64
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  1.098,9  +43,3 -46,0 |  58.2 / 64.6    +2.4 -2.3 |  44.7      | 69.76                | 89.09               | 58      | 11684712   |
| TRT_fp32        |  1.096,0  +132,8 -162,5 |  58.4 / 68.4    +8.1 -7.5 |  51.7      | 69.76                | 89.09               | 30      | 11678912   |
| TRT_fp16        |  2.727,4  +305,6 -367,6 |  23.5 / 30.7    +3.0 -2.8 |  22.8      | 69.76                | 89.10               | 27      | 11678912   |
| TRT_int8        |  3.889,1  +477,0 -585,0 |  16.5 / 24.4    +2.3 -2.2 |  11.7      | 69.53                | 88.96               | 25      | 11669504   |
 
# resnet18 bs 128
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  1.096,2  +31,3 -32,7 | 116.8 / 122.6   +3.4 -3.4 |  44.7      | 69.80                | 89.10               | 58      | 11684712   |
| TRT_fp32        |  1.070,8  +37,6 -39,7 | 119.5 / 126.3   +4.4 -4.3 |  51.7      | 69.80                | 89.10               | 30      | 11678912   |
| TRT_fp16        |  3.135,7  +539,9 -728,8 |  40.8 / 54.1    +8.5 -7.7 |  22.8      | 69.80                | 89.11               | 27      | 11678912   |
| TRT_int8        |  4.216,7  +583,6 -737,2 |  30.4 / 37.5    +4.9 -4.5 |  11.7      | 69.57                | 88.98               | 25      | 11669504   |
 
# resnet18 bs 256
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  1.117,1  +26,4 -27,4 | 229.2 / 237.8   +5.5 -5.5 |  44.7      | 69.80                | 89.10               | 58      | 11684712   |
| TRT_fp32        |  1.045,2  +31,3 -32,8 | 244.9 / 258.9   +7.6 -7.4 |  51.7      | 69.80                | 89.10               | 30      | 11678912   |
| TRT_fp16        |  3.322,4  +423,6 -524,3 |  77.1 / 100.3   +11.3 -10.5 |  22.8      | 69.80                | 89.11               | 27      | 11678912   |
| TRT_int8        |  4.671,2  +625,3 -783,1 |  54.8 / 72.2    +8.5 -7.9 |  11.7      | 69.57                | 88.98               | 25      | 11669504   |
 
# resnet34 bs 1
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  223,2  +17,6 -20,0 |   4.5 / 8.1     +0.4 -0.4 |  83.3      | 73.30                | 91.42               | 93      | 21789160   |
| TRT_fp32        |  374,1  +15,1 -16,1 |   2.7 / 4.2     +0.1 -0.1 |  125.5     | 73.30                | 91.42               | 45      | 21779648   |
| TRT_fp16        |  813,6  +68,4 -78,3 |   1.2 / 4.6     +0.1 -0.1 |  44.2      | 73.31                | 91.42               | 47      | 21779648   |
| TRT_int8        |  928,7  +92,1 -108,3 |   1.1 / 2.4     +0.1 -0.1 |  23.0      | 73.31                | 91.33               | 41      | 21770240   |
 
# resnet34 bs 32
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  647,1  +14,9 -15,5 |  49.5 / 54.7    +1.2 -1.2 |  83.3      | 73.31                | 91.42               | 98      | 21789160   |
| TRT_fp32        |  578,6  +10,6 -10,9 |  55.3 / 59.1    +1.0 -1.0 |  106.3     | 73.31                | 91.42               | 46      | 21779648   |
| TRT_fp16        |  1.943,0  +266,4 -335,8 |  16.5 / 21.9    +2.6 -2.4 |  42.1      | 73.31                | 91.44               | 46      | 21779648   |
| TRT_int8        |  2.741,0  +252,4 -293,0 |  11.7 / 15.4    +1.2 -1.1 |  21.4      | 73.23                | 91.34               | 41      | 21770240   |
 
# resnet34 bs 64
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  672,4  +13,1 -13,5 |  95.2 / 99.8    +1.9 -1.9 |  83.3      | 73.31                | 91.42               | 98      | 21789160   |
| TRT_fp32        |  578,8  +10,3 -10,6 | 110.6 / 115.7   +2.0 -2.0 |  106.3     | 73.31                | 91.42               | 46      | 21779648   |
| TRT_fp16        |  2.377,5  +257,5 -307,7 |  26.9 / 33.2    +3.3 -3.1 |  42.1      | 73.31                | 91.44               | 46      | 21779648   |
| TRT_int8        |  2.932,4  +258,0 -297,4 |  21.8 / 28.9    +2.1 -2.0 |  21.4      | 73.23                | 91.34               | 41      | 21770240   |
 
# resnet34 bs 128
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  680,0  +11,5 -11,8 | 188.2 / 193.8   +3.2 -3.2 |  83.3      | 73.35                | 91.43               | 98      | 21789160   |
| TRT_fp32        |  584,8  +12,5 -12,9 | 218.9 / 235.9   +4.8 -4.7 |  106.3     | 73.35                | 91.43               | 46      | 21779648   |
| TRT_fp16        |  2.457,4  +250,6 -296,1 |  52.1 / 63.9    +5.9 -5.6 |  42.1      | 73.35                | 91.45               | 46      | 21779648   |
| TRT_int8        |  3.449,5  +667,2 -941,1 |  37.1 / 49.2    +8.9 -8.0 |  21.4      | 73.27                | 91.35               | 41      | 21770240   |
 
# resnet34 bs 256
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  685,9  +11,9 -12,2 | 373.2 / 384.8   +6.6 -6.5 |  83.3      | 73.35                | 91.43               | 98      | 21789160   |
| TRT_fp32        |  579,9  +11,7 -12,1 | 441.4 / 454.7   +9.1 -9.0 |  106.3     | 73.35                | 91.43               | 46      | 21779648   |
| TRT_fp16        |  2.274,2  +144,2 -159,4 | 112.6 / 123.0   +7.6 -7.4 |  42.1      | 73.35                | 91.45               | 46      | 21779648   |
| TRT_int8        |  3.631,3  +519,3 -661,9 |  70.5 / 93.0    +11.8 -10.9 |  21.4      | 73.27                | 91.35               | 41      | 21770240   |
 
# resnet50 bs 1
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  181,1  +15,3 -17,5 |   5.5 / 11.3    +0.5 -0.5 |  97.8      | 80.35                | 95.13               | 126     | 25530472   |
| TRT_fp32        |  303,8  +10,4 -11,0 |   3.3 / 4.6     +0.1 -0.1 |  107.1     | 80.35                | 95.13               | 97      | 25502912   |
| TRT_fp16        |  759,0  +50,8 -56,5 |   1.3 / 3.5     +0.1 -0.1 |  50.1      | 80.37                | 95.13               | 64      | 25502912   |
| TRT_int8        |  924,4  +84,3 -97,7 |   1.1 / 2.7     +0.1 -0.1 |  27.2      | 78.59                | 94.96               | 58      | 25493504   |
 
# resnet50 bs 32
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  347,1  +3,2 -3,2 |  92.2 / 94.9    +0.8 -0.8 |  97.8      | 80.36                | 95.13               | 131     | 25530472   |
| TRT_fp32        |  455,4  +6,3 -6,5 |  70.3 / 74.1    +1.0 -1.0 |  108.1     | 80.36                | 95.13               | 60      | 25502912   |
| TRT_fp16        |  1.761,4  +136,2 -154,2 |  18.2 / 22.1    +1.5 -1.5 |  49.5      | 80.36                | 95.12               | 60      | 25502912   |
| TRT_int8        |  2.247,7  +196,5 -226,3 |  14.2 / 21.0    +1.4 -1.3 |  25.5      | 79.81                | 95.07               | 58      | 25493504   |
 
# resnet50 bs 64
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  357,5  +2,8 -2,9 | 179.0 / 183.3   +1.4 -1.4 |  97.8      | 80.36                | 95.13               | 131     | 25530472   |
| TRT_fp32        |  457,1  +9,0 -9,3 | 140.0 / 145.8   +2.8 -2.8 |  108.1     | 80.36                | 95.13               | 60      | 25502912   |
| TRT_fp16        |  1.784,9  +143,8 -163,7 |  35.9 / 41.8    +3.1 -3.0 |  49.5      | 80.36                | 95.12               | 60      | 25502912   |
| TRT_int8        |  2.640,6  +352,4 -441,1 |  24.2 / 32.9    +3.7 -3.5 |  25.5      | 79.81                | 95.07               | 58      | 25493504   |
 
# resnet50 bs 128
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  361,0  +2,6 -2,6 | 354.6 / 361.2   +2.6 -2.5 |  97.8      | 80.39                | 95.13               | 131     | 25530472   |
| TRT_fp32        |  461,0  +7,7 -7,9 | 277.6 / 285.6   +4.7 -4.7 |  108.1     | 80.39                | 95.13               | 60      | 25502912   |
| TRT_fp16        |  1.811,5  +109,8 -120,9 |  70.7 / 81.2    +4.6 -4.4 |  49.5      | 80.39                | 95.13               | 60      | 25502912   |
| TRT_int8        |  2.948,1  +279,3 -325,7 |  43.4 / 53.1    +4.5 -4.3 |  25.5      | 79.85                | 95.08               | 58      | 25493504   |
 
# resnet50 bs 256
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  361,9  +2,2 -2,2 | 707.3 / 714.1   +4.2 -4.2 |  97.8      | 80.39                | 95.13               | 131     | 25530472   |
| TRT_fp32        |  459,6  +7,5 -7,7 | 557.0 / 587.3   +9.2 -9.1 |  108.1     | 80.39                | 95.13               | 60      | 25502912   |
| TRT_fp16        |  1.683,3  +79,0 -85,0 | 152.1 / 166.1   +7.5 -7.3 |  49.5      | 80.39                | 95.13               | 60      | 25502912   |
| TRT_int8        |  2.911,8  +274,3 -319,7 |  87.9 / 115.2   +9.1 -8.7 |  25.5      | 79.85                | 95.08               | 58      | 25493504   |
 
# resnet101 bs 1
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  104,0  +8,3 -9,4 |   9.6 / 16.3    +0.8 -0.8 |  170.5     | 81.67                | 95.66               | 245     | 44496488   |
| TRT_fp32        |  166,0  +4,3 -4,4 |   6.0 / 7.0     +0.2 -0.2 |  209.5     | 81.67                | 95.66               | 172     | 44442816   |
| TRT_fp16        |  431,4  +18,1 -19,3 |   2.3 / 4.1     +0.1 -0.1 |  88.0      | 81.65                | 95.67               | 111     | 44442816   |
| TRT_int8        |  590,8  +33,5 -36,6 |   1.7 / 3.8     +0.1 -0.1 |  46.0      | 79.91                | 95.58               | 109     | 44433408   |
 
# resnet101 bs 32
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  209,4  +1,7 -1,7 | 152.8 / 156.0   +1.2 -1.2 |  170.5     | 81.68                | 95.66               | 250     | 44496488   |
| TRT_fp32        |  256,0  +2,5 -2,5 | 125.0 / 127.4   +1.2 -1.2 |  210.3     | 81.68                | 95.66               | 111     | 44442816   |
| TRT_fp16        |  1.133,1  +118,5 -140,7 |  28.2 / 33.9    +3.3 -3.1 |  85.8      | 81.66                | 95.66               | 150     | 44442816   |
| TRT_int8        |  1.850,4  +203,1 -243,3 |  17.3 / 21.7    +2.1 -2.0 |  44.2      | 80.78                | 95.64               | 109     | 44433408   |
 
# resnet101 bs 64
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  218,1  +1,1 -1,1 | 293.5 / 297.4   +1.5 -1.5 |  170.5     | 81.68                | 95.66               | 250     | 44496488   |
| TRT_fp32        |  260,2  +2,1 -2,2 | 246.0 / 251.0   +2.0 -2.0 |  210.3     | 81.68                | 95.66               | 111     | 44442816   |
| TRT_fp16        |  1.173,8  +115,5 -135,6 |  54.5 / 61.2    +6.0 -5.6 |  85.8      | 81.66                | 95.66               | 150     | 44442816   |
| TRT_int8        |  2.020,4  +190,2 -221,6 |  31.7 / 37.2    +3.3 -3.1 |  44.2      | 80.78                | 95.64               | 109     | 44433408   |
 
# resnet101 bs 128
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  219,9  +0,9 -0,9 | 582.0 / 586.1   +2.4 -2.4 |  170.5     | 81.71                | 95.66               | 250     | 44496488   |
| TRT_fp32        |  262,3  +2,6 -2,6 | 487.9 / 494.9   +4.9 -4.9 |  210.3     | 81.71                | 95.66               | 111     | 44442816   |
| TRT_fp16        |  1.146,8  +35,3 -37,0 | 111.6 / 119.3   +3.5 -3.5 |  85.8      | 81.69                | 95.66               | 150     | 44442816   |
| TRT_int8        |  2.118,8  +156,3 -175,8 |  60.4 / 66.2    +4.8 -4.6 |  44.2      | 80.82                | 95.65               | 109     | 44433408   |
 
# resnet101 bs 256
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  220,5  +0,9 -1,0 | 1161.1 / 1169.6  +5.0 -5.0 |  170.5     | 81.71                | 95.66               | 250     | 44496488   |
| TRT_fp32        |  262,0  +2,7 -2,8 | 977.2 / 1011.2  +10.2 -10.2 |  210.3     | 81.71                | 95.66               | 111     | 44442816   |
| TRT_fp16        |  1.113,0  +49,2 -52,7 | 230.0 / 254.6   +10.6 -10.4 |  85.8      | 81.69                | 95.66               | 150     | 44442816   |
| TRT_int8        |  1.917,9  +106,5 -116,2 | 133.5 / 142.3   +7.8 -7.6 |  44.2      | 80.82                | 95.65               | 109     | 44433408   |
 
# resnet152 bs 1
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  71,9  +4,3 -4,7 |  13.9 / 22.8    +0.9 -0.9 |  230.5     | 82.35                | 95.92               | 364     | 60117096   |
| TRT_fp32        |  114,9  +6,9 -7,6 |   8.7 / 30.6    +0.6 -0.5 |  291.9     | 82.35                | 95.92               | 258     | 60040384   |
| TRT_fp16        |  319,9  +10,9 -11,5 |   3.1 / 5.2     +0.1 -0.1 |  116.1     | 82.32                | 95.92               | 166     | 60040384   |
| TRT_int8        |  430,2  +19,0 -20,4 |   2.3 / 6.8     +0.1 -0.1 |  61.5      | 79.96                | 95.74               | 160     | 60030976   |
 
# resnet152 bs 32
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  147,6  +0,9 -0,9 | 216.8 / 219.3   +1.3 -1.3 |  230.5     | 82.35                | 95.92               | 369     | 60117096   |
| TRT_fp32        |  177,7  +1,4 -1,4 | 180.1 / 182.8   +1.4 -1.4 |  294.6     | 82.35                | 95.92               | 162     | 60040384   |
| TRT_fp16        |  806,1  +63,0 -71,4 |  39.7 / 44.2    +3.4 -3.2 |  116.0     | 82.34                | 95.91               | 252     | 60040384   |
| TRT_int8        |  1.449,9  +141,3 -165,6 |  22.1 / 26.2    +2.4 -2.3 |  59.9      | 81.80                | 95.81               | 160     | 60030976   |
 
# resnet152 bs 64
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  153,8  +0,6 -0,6 | 416.2 / 421.4   +1.5 -1.5 |  230.5     | 82.35                | 95.92               | 369     | 60117096   |
| TRT_fp32        |  181,3  +1,2 -1,2 | 353.0 / 356.5   +2.3 -2.3 |  294.6     | 82.35                | 95.92               | 162     | 60040384   |
| TRT_fp16        |  833,0  +40,1 -43,3 |  76.8 / 82.0    +3.9 -3.8 |  116.0     | 82.34                | 95.91               | 252     | 60040384   |
| TRT_int8        |  1.539,3  +173,2 -208,6 |  41.6 / 50.1    +5.3 -5.0 |  59.9      | 81.80                | 95.81               | 160     | 60030976   |
 
# resnet152 bs 128
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  155,0  +0,4 -0,4 | 825.9 / 830.1   +2.4 -2.4 |  230.5     | 82.39                | 95.92               | 369     | 60117096   |
| TRT_fp32        |  183,0  +0,9 -0,9 | 699.4 / 705.2   +3.3 -3.3 |  294.6     | 82.39                | 95.92               | 162     | 60040384   |
| TRT_fp16        |  821,3  +21,6 -22,5 | 155.9 / 164.5   +4.2 -4.2 |  116.0     | 82.38                | 95.91               | 252     | 60040384   |
| TRT_int8        |  1.537,3  +79,2 -85,9 |  83.3 / 96.5    +4.5 -4.4 |  59.9      | 81.84                | 95.82               | 160     | 60030976   |
 
# resnet152 bs 256
 
CUDA is available.
|  Model          | inf/s +-95% | Latency (ms) +-95%|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)| #layers | #parameters|
|-----------------|-------------|-----------------------|-----------|----------------------|---------------------|---------|------------|
| Vanilla         |  155,2  +0,4 -0,5 | 1649.2 / 1656.0  +4.8 -4.8 |  230.5     | 82.39                | 95.92               | 369     | 60117096   |
| TRT_fp32        |  182,9  +1,0 -1,0 | 1399.4 / 1411.1  +7.4 -7.4 |  294.6     | 82.39                | 95.92               | 162     | 60040384   |
| TRT_fp16        |  828,5  +19,8 -20,5 | 309.0 / 321.3   +7.6 -7.5 |  116.0     | 82.38                | 95.91               | 252     | 60040384   |
| TRT_int8        |  1.448,8  +56,1 -59,6 | 176.7 / 188.1   +7.1 -7.0 |  59.9      | 81.84                | 95.82               | 160     | 60030976   |
 