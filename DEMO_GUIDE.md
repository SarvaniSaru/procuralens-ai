# Demo Guide

## Successful run
1. Run `python scripts/init_db.py` and `streamlit run ProcureLens.py`.
2. Choose Demo Mode, select the seeded project, and load bundled PDFs.
3. Run evaluation, inspect page-linked evidence, complete an SME adjustment, approve scores, and open Results.
4. Review the leaderboard and spider plot, then download JSON.

## Validation/error run
Use the validation tests or a mocked malformed provider response. Confirm that warnings are visible and that normalization/fallback remains deterministic and traceable.
