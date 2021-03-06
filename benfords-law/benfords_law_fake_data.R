#! /usr/bin/env Rscript

library("benford.analysis")
data("census.2009")                      # População das Cidades dos Estados Unidos - 2009

bfd_barplot <- function(benford){
  barplot(benford$bfd$data.dist.freq,
          names.arg = bfd$bfd$digits,
          col = "#A1DCF0",
          main = "Digits Distribution",
          xlab = "Digits", ylab = "Freq",
          ylim = range(0:max(benford$bfd$data.dist.freq)),
          xlim = range(0:length(bfd$bfd$benford.dist)),
          width = .85)
  lines(x = benford$bfd$benford.dist.freq, col = "red", lwd=2.5)
}

bfd <- benford(census.2009$pop.2009, number.of.digits = 1)
p <- bfd$bfd$benford.dist                # probabilidades para 1 primeiro digito

png(filename="benford-fake-data-1-digit.png",
    width=1100,
    height=285)

par(mfrow=c(1,3))
for(size in c(10, 100, 1000)){
  data <- sample(c(1:9), size=size, prob = p, replace=TRUE)
  fake_data_bfd <- benford(data, number.of.digits = 1)
  bfd_barplot(fake_data_bfd)
}

dev.off()

bfd <- benford(census.2009$pop.2009, number.of.digits = 2)
p <- bfd$bfd$benford.dist               # probabilidades para 2 primeiros digitos

png(filename="benford-fake-data-2-digits.png",
    width=1100,
    height=285)

par(mfrow=c(1,3))
for(size in c(100, 1000, 10000)){
  data <- sample(c(10:99), size=size, prob = p, replace=TRUE)
  fake_data_bfd <- benford(data, number.of.digits = 2)
  bfd_barplot(fake_data_bfd)
}

dev.off()
