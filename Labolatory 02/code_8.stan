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
    // using the vectorized log probability destiny
    target += normal_lpdf(y | theta, 1);

    // Add marginal probability destiny for theta
    // to the joint log probability destiny
    target += normal_lpdf(theta | 0, 1);
}