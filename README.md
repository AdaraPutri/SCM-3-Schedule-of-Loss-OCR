# SCM-3-Schedule-of-Loss-OCR
OCR tool that turns receipt and invoice photos into a Schedule of Loss spreadsheet. Admins upload the images and it extracts vendor, purchase date, line items, and prices into Excel, cutting the hours or weeks of manual transcription that currently goes into every large claim.

### Set Up Instructions
Run the following:

1. Create and enter virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install the dependencies
```bash
pip install -r requirements.txt
```

3. Connect AWS account
```bash
aws configure
```
Insert the AWS access key ID and secret access key when prompted. Enter the options below.
Default region name:
```bash
us-east-1
```
Default output format:
```bash
json
```

### Testing
1. Generate sample receipts to test on. Use this dataset:
[https://expressexpense.com/blog/free-receipt-images-ocr-machine-learning-dataset](https://expressexpense.com/blog/free-receipt-images-ocr-machine-learning-dataset/)