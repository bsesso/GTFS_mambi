# Numéro de ônibus passando por cada ponto de SP


## Arquivos gerados
O arquivo final de pontos de onibus e o número de onibus passando por dia em cada um deles é o:
[buses\_on\_stop.txt](buses_on_stop.txt)

O de trens é:
trains\_on\_stop.txt](trains_on_stop.txt)

Além disso eu gerei os seguintes arquivos:

| Arquivo | Descrição |
| ------- | --------- |
| [buses\_on\_stop.txt](buses_on_stop.txt) | Numero de onibus passando por ponto por dia, **separados por uma virgula** |
| [buses\_on\_stop\_readable.txt](buses\_on\_stop\_readable.txt) | Mesmo que acima, mas de **forma mais legível** |
| [buses\_on\_stop\_readable\_complete.txt](buses\_on\_stop\_readable\_complete.txt) | Mesmo que acima, mas **incluindo calculos** |
| [trains\_on\_stop.txt](trains_on_stop.txt) | Numero de trens passando por ponto por dia, **separados por uma virgula** |
| [trains\_on\_stop\_readable.txt](trains\_on\_stop\_readable.txt) | Mesmo que acima, mas de **forma mais legível** |
| [trains\_on\_stop\_readable\_complete.txt](trains\_on\_stop\_readable\_complete.txt) | Mesmo que acima, mas **incluindo calculos** |
| [departures.txt](departures.txt) | Número de onibus de determinada linha que saem em um periodo de um dia **separados por uma virgula**  |
| [departures_readable.txt](departures_readable.txt) | Mesmo que acima, mas de forma **mais legível** |
| [departures_readable_complete.txt](departures_readable_complete.txt) | Mesmo que acima, mas **incluindo calculos** |


## Código fonte
Está dentro da pasta [src](src/) e foi escrito usando Python 3.
Para rodar use:
```sh
python main.py [arquivo de frequencies] [arquivo de stop_times]
```

#### Exemplo 
```sh
python main.py ../GTFS/frequencies.txt ../GTFS/stop_times.txt
```


