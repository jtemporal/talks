#! /usr/bin/env Rscript

require("benford.analysis")              # Carregando o pacote necessário
data("census.2009")                      # População das Cidades dos Estados Unidos - 2009
bfd <- benford(census.2009$pop.2009,     # Coluna com o censo por cidade em 2009
               number.of.digits = 1)     # Número de Primeiros Dígitos para analisar

png(filename="benford-population-us.png",
    width=780,
    height=650)

plot(bfd)

dev.off()

png(filename="digits-distribution-population-us.png",
    width=780,
    height=650)

barplot(bfd$bfd$data.dist.freq,          # Valores de frequencia para cada barra
        names.arg = bfd$bfd$digits,      # Legenda de cada barra no eixo x
        col = "#A1DCF0",                 # Coloração das barras
        main = "Digits Distribution",    # Título principal
        xlab = "Digits",                 # Legenda eixo x
        ylab = "Freq",                   # Legenda eixo y
        ylim = range(0:6000),            # Limite no eixo y
        xlim = range(0:10),              # Limite no eixo x
        width = .85)                     # Largura da barra

lines(x = bfd$bfd$benford.dist.freq,     # Pontos para formar a linha
      col = "red",                       # Cor da linha
      lwd=2.5,                           # Espessura da linha
      type="c")                          # Tipo da linha: tracejado

dev.off()
