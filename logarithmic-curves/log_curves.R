#! /usr/bin/env Rscript

png(filename="log-x-curve.png",
    width=780,
    height=780)
curve(log(x), 1, 100, col = "red", lwd=2, main="Logarithmic Curve")
dev.off()

png(filename="log-1-over-x-curve.png",
    width=780,
    height=780)
curve(log(1/x), 1, 100, col = "red", lwd=2, main="Logarithmic Curve")
dev.off()

png(filename="log-1-minus-1-over-x-curve.png",
    width=780,
    height=780)
curve(log(1 - 1/x), 1, 100, col = "red", lwd=2, main="Logarithmic Curve")
dev.off()

png(filename="log-1-plus-1-over-x-curve.png",
    width=780,
    height=780)
curve(log(1 + 1/x), 1, 100, col = "red", lwd=2, main="Logarithmic Curve")
dev.off()
