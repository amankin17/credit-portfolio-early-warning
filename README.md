# Credit Portfolio Early-Warning Monitor

**Focus:** credit risk · portfolio analytics · segmented KPI reporting · explainable rules

An offline prototype that generates **synthetic loan accounts**, scores a simple, transparent early-warning rule, and produces a segment-level summary. This is a decision-support demonstration, **not** a validated credit scoring model and should never be used to approve or deny borrowers.

## Run
```bash
python src/monitor.py
python -m unittest discover -s tests -v
```

## Features
- Deterministic synthetic portfolio across three loan products.
- Rule-based flags for 30+ days past due, high utilisation, and high payment-to-income ratio.
- Product-level exposure, flagged accounts and arrears rate.
- Tests for rule boundaries and portfolio arithmetic.

## Methodological boundaries
The synthetic population is not representative, labels are not outcomes, and the heuristic's predictive performance has **not** been established. Real deployment requires legal/compliance review, governance, bias testing, securely sourced historic outcomes, calibration, monitoring and analyst oversight.

## Business question
Which segments show rising arrears and need investigation? Future work can add monthly snapshots and vintage analysis to distinguish portfolio aging from deteriorating quality.

See [ROADMAP.md](ROADMAP.md) for forward-looking stages.
