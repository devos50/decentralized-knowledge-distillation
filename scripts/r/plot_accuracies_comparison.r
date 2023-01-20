library(ggplot2)
library(dplyr)

dat <- read.csv("../../data/accuracies_comparison.csv")
dat$peers <- as.factor(dat$peers)

dat <- dat %>%
  group_by(dataset, algorithm, peers) %>%
  summarise(acc = mean(accuracy), acc_sd = sd(accuracy))

print(dat)

p <- ggplot(dat, aes(x=peers, y=acc, group=algorithm, color=algorithm)) +
    geom_line() +
    geom_point(aes(shape=algorithm)) +
    geom_errorbar(aes(ymin=acc-acc_sd, ymax=acc+acc_sd)) +
    xlab("Peers") +
    ylab("Test Accuracy") +
    theme_bw() +
    theme(legend.position=c(0.17, 0.3), legend.box.background = element_rect(colour = "black"), legend.title=element_blank())

ggsave("../../plots/accuracies_comparison.pdf", p, width=5, height=3)