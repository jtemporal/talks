# Lei de Benford

Um projeto simples sobre algumas analises de utilizando a Lei de Benford.

## Instalação

Instale o R ([detalhes de como fazer isso podem ser encontrados no site oficial do R](https://cran.r-project.org/)).

e no terminal rode o comando abaixo para instalar o pacote necessario:
```console
$ Rscript install_packages.R
```

Aqui vamos usar o pacote [`benford.analysis`](https://github.com/carloscinelli/benford.analysis)

## Arquivos

- `install_packages.R`: Para instalar as dependencias
- `benfords_law.R`: Rscript que gera os plots de para os dado do censo de 2019 para as cidades dos Estados Unidos
- `benfors_law.Rmd` mesmo que o arquivo anterior mas no formato RMarkdown para ser utilizado no RStudio

## Usando o script

No seu terminal rode:

```console
$ Rscript benfords_law.R
```
