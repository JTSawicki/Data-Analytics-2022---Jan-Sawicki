data {
    int<lower=1> N; // Number of observations
}

generated quantities {
   real mu = normal_rng(0,1);
   real<lower=0> sigma = abs(normal_rng(0,1));

   array[N] real y_prior;
   for(i in 1:N) {
       y_prior[i] = normal_rng(mu, sigma);
   }
}