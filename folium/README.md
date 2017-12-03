# Usando a biblioteca Folium

Um projeto simples sobre algumas análises de utilizando a biblioteca [Folium]().

## Instalação

### Docker 🐳

Instale o [docker](https://docs.docker.com/engine/installation/) e o [docker-compose](https://docs.docker.com/compose/install/). Depois disso é só rodar:

_Pode ser que esse comando demore um pouco na primeira vez_
```console
$ docker-compose up
```

### Local

**TODO**

## Dados

No notebook vou usar os dados de geolocalização de empresas no Brasil. O arquivo original,  gerado pelo Serenata, pode ser baixado pelo `serenata-toolbox` e instruções sobre como fazer isso podem ser encontradas [aqui](https://github.com/datasciencebr/serenata-toolbox/blob/master/README.rst#usage).

## Arquivos

- `prepacao-de-dados.ipynb`: Apenas um registro de como o dataset foi feito
- `folium.ipynb`: Análise usando a biblioteca folium
- `mapas/`: Diretório com os mapas resultantes da análise
- `empresas.xz`: Arquivo `.csv` comprimido com dados de empresas
