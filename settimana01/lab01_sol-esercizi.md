# Lab 01

## Parte 1

### Es 01.1.1: Appuntamenti

```
Se start1 > start2 
s = start1 

Altrimenti
s = start2 

Se end1 < end2
e = end1 
Altrimenti e = end2 

Se s < e 
Gli appuntamenti si sovrappongono 
Altrimenti Gli appuntamenti non si sovrappongono
```
---
```mermaid
flowchart TD
start([start])-->
input[/"`
    start1, start2
    end1, end2`"/]-->
A{start1 > start2}
A--true-->AT[s = start1]
A--false-->AF[s = start2]
AF-->B
AT-->B{end1 < end2}
B--true-->BT[e = end1]
B--false-->BF[e = end2]-->C
BT-->C{s < e}--true-->CT[si sovrappongono]
C--false-->CF[non si sovrappongono]
CT-->stop([stop])
CF-->stop

```

### Es 01.1.2: Stagioni

### Es 01.1.3: Sulla strada

![soluzione](sol-es01.1.3.png)

### Es 01.1.4: Piastrelle

![soluzione](sol-es01.1.4.png)