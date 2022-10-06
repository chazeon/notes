---
title: Hypothesis testing
---

Given a limited number of samples, see *how likely* the hypothesis are true. Both Z test and t test aims to convert the *sample statistics* to *population statistics*.

## Definitions

Given the population mean $\mu$, sample mean $\bar X$.

### Z test

Standard score

$$
Z = \frac{\bar X - \mu}{\sigma}
$$

### $t$-test

$$
t = \frac{\bar X - \mu}{\sigma / \sqrt{n}}
$$

### Comparison

## Implementations

In Python, $t$-test is impmented in [`scipy.stats`](https://docs.scipy.org/doc/scipy/reference/stats.html) as `scipy.stats.t` `scipy.stats.ttest_ind_xxx`.

## References

- [Hypothesis Testing | Difference between Z-Test and T-Test](https://www.analyticsvidhya.com/blog/2020/06/statistics-analytics-hypothesis-testing-z-test-t-test/)
- [Student's t-test - Wikipedia](https://en.wikipedia.org/wiki/Student's_t-test)
- [Z-test - Wikipedia](https://en.wikipedia.org/wiki/Z-test)

