# Schedule of Loss OCR — notes

Two separate versions. One is to develop my skills, the other one is to be used by colleagues (aligns with company privacy policy).

## 1. Cloud portfolio project (separate repo, fake data only)

- S3 — upload trigger
- Lambda (Python)
- Textract (AWS's own OCR, instead of Azure — one provider, simpler story)
- MySQL or skip the DB — this data doesn't need NoSQL
- openpyxl for the export
- Postman to test Textract/Lambda while building
- Terraform later, if at all

Build order:
1. S3 alone (console, then boto3)
2. Lambda alone, triggered manually
3. S3 upload auto-triggers Lambda
4. Lambda calls Textract, gets JSON back
5. Write result to MySQL and/or generate the xlsx

## 2. Local tool (actual work tool)

- Tesseract.js — OCR in the browser, nothing leaves the machine
- SheetJS (xlsx) — fills the real template client-side, keeps formulas/formatting
- Plain HTML/CSS/JS, no framework, no build step
- Static files, run locally or host on an internal server
- No backend, no network calls

Build order:
1. Local server + skeleton page (understand why file:// breaks fetch())
2. Static UI, no logic
3. File upload / drag-drop
4. Tesseract.js on one image, log raw text
5. parser.js — regex for vendor/date/price, tested on its own first
6. Editable review table
7. SheetJS export into the real template
8. Edge cases (50-row limit, bad files, empty states)
9. Test pass
10. UI polish
11. One-pager for IT: what it touches, what it doesn't, dependency licenses