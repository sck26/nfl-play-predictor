# NFL Play Predictor — Rule-Based Web Demo

> **Status: Source code published; AWS deployment unverified.** This repository is a lightweight demonstration of a football play-call heuristic, **not** the trained gradient-boosting NFL model. Do not use it as proof of an 80% accuracy result or a live AWS deployment.

## What is implemented

- Responsive interactive site: [site/index.html](site/index.html)
- Python JSON endpoint compatible with AWS Lambda: [lambda_api/app.py](lambda_api/app.py)
- Basic unit tests: [tests/test_app.py](tests/test_app.py)
- Deployment instructions: [deploy/AWS_SETUP.md](deploy/AWS_SETUP.md)
- Browser-side fallback when the API is not configured

## Verified deployment status

| Component | Status | Live URL |
| --- | --- | --- |
| GitHub source | Published | https://github.com/sck26/nfl-play-predictor |
| AWS S3 website | **Not verified as deployed** | Not provided |
| AWS Lambda API | **Not verified as deployed** | Not provided |

In particular, `site/index.html` currently sets `const API_URL='';`, so the interactive demo uses local JavaScript rules rather than a live Lambda endpoint. Publishing to GitHub does **not** deploy either AWS service.

## Run locally

Open `site/index.html` in a browser.

Run the unit tests:

```bash
python -m unittest discover -s tests -v
```

Run the API handler locally:

```bash
python -m lambda_api.app
```

For a Lambda test event:

```json
{"requestContext":{"http":{"method":"GET"}},"queryStringParameters":{"down":"3","distance":"8"}}
```

Example JSON response:

```json
{"prediction":"pass","down":3,"distance":8,"model":"rule-based-demo","disclaimer":"Educational heuristic, not a trained ML prediction."}
```

## Deploy to AWS

Follow [the deployment guide](deploy/AWS_SETUP.md). After deploying:

1. Confirm the S3 website opens.
2. Confirm a request to the actual Lambda function URL returns HTTP 200 and valid JSON.
3. Set `API_URL` in `site/index.html` to that function URL, deploy the website again, and test the full UI.
4. **Only then** replace the two 'Not verified' entries in this README with actual public endpoints and verification details.

Never commit credentials. An exposed public API may incur charges; check account requirements and costs before deployment.

## How this relates to an NFL machine-learning model

This project contains **no gradient-boosting training code, training dataset, train/test split, or measured evaluation metrics**. The rule-based output is not a statistically validated prediction.

A separate trained model repository should document its data source, target labels, engineered features, preprocessing, train/test split, training code, evaluation results (including confusion matrix and class balance where relevant), and reproducibility instructions. Any reported **80% result must be backed by that model's recorded evaluation**, not assigned to this demo.

## Resume guidance

Until AWS is verified, describe this only as a **Python rule-based API and JavaScript football play-call demo**, not as an S3/Lambda deployment or an 80%-accurate ML predictor.

## License

MIT. See [LICENSE](LICENSE).
