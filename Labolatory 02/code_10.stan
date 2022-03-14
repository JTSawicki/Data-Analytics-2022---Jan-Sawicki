data {
    int<lower=1> N; // Number of ys
}

parameters {
    real y[N]; // Probabilistic variables y
    real theta; // Probabilistic variable theta
}

model {
    // Add conditional probability destiny for the ys
    // given theta to the joint log probability destiny
    // using equivalent sampling statement
    y ~ normal(theta, 1);

    // Add marginal probability destiny for theta
    // to the joint log probability destiny using
    // equivalent sampling statement
    theta ~ normal(0, 1);
}

generated quantities {
   real mean_y = mean(y);
}