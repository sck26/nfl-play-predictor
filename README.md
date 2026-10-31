# Fourth Down Lab — NFL Play Predictor Demo

An interactive football play-type **rule-based prototype**, with a Python serverless API designed for AWS Lambda. This is a portfolio demonstration, not a trained machine learning model.

## Features
- Responsive static website in `site/index.html`
- Down and yards-to-gain inputs with a play recommendation
- Python Lambda API with JSON responses and CORS headers
- Browser-only fallback before deployment
- Unit tests and an AWS deployment guide

## Local development
Open `site/index.html` in a browser. No frontend dependencies are needed.

Run tests from the repository root:
```bash
python -m unittest discover -s tests -v
```

Test the API locally:
```bash
python -m lambda_api.app
```

## API
After deploying AWS Lambda with a Function URL:
`GET https://YOUR_FUNCTION_URL/?down=3&distance=8`

Example response:
```json
{"prediction":"pass","down":3,"distance":8,"model":"rule-based-demo","disclaimer":"Educational heuristic, not a trained ML prediction."}
```

## AWS
Follow [AWS_SETUP.md](deploy/AWS_SETUP.md). Once Lambda is live, replace `const API_URL='';` in `site/index.html` with its HTTPS URL, then upload the website to S3.

## Accuracy and resume claims
This demo has **no measured model accuracy**, and it should not be described as AWS-deployed until the services are actually deployed. Do not attribute an 80% figure to this heuristic. After deployment, S3 and Lambda can accurately be listed in the project description.

## Security
Do not commit credentials. Public endpoints can incur usage costs. Review AWS pricing and free-plan terms, enable MFA, monitor usage and ask a parent or guardian for help with account/billing requirements if applicable.

## License
MIT. See [LICENSE](LICENSE).
