# Contributing to BD Patient Journey Analytics

Thank you for contributing. This repository is a public, synthetic healthcare-operations and analytics project. Contributions should improve reproducibility, clarity, governance, analytical quality, or operational usefulness without introducing real patient data.

## Before you start

Please review:

- `README.md` for project scope and architecture;
- `PROJECT_CHARTER.md` for the management decision question;
- `ROADMAP.md` for version direction;
- `DATA_PROVENANCE.md` and `DATASET_USAGE_GUIDE.md` for data rules;
- `SECURITY.md` for privacy and security boundaries; and
- `CODE_OF_CONDUCT.md` for community expectations.

## Contribution principles

1. **Synthetic data only.** Never commit real patient-identifying information, biometric templates, credentials, bank details, private clinical records, or other sensitive personal data.
2. **Keep clinical boundaries clear.** AI and analytics in this repository support operations, routing, forecasting, staffing, billing, and workflow design. They do not replace qualified clinical judgement.
3. **Prefer reproducible work.** Analytical changes should state data inputs, assumptions, methodology, and expected output.
4. **Keep human override auditable.** Routing or prioritization logic should preserve a clear manual override path where relevant.
5. **Document material assumptions.** Financial, workforce, queue, SLA, and predictive models should explain assumptions and limitations.
6. **Do not misrepresent synthetic outputs.** Demonstration results must not be described as verified results from a real hospital implementation.

## Recommended workflow

1. Open or identify an issue describing the problem or proposed improvement.
2. Create a focused branch using the repository naming convention, for example:
   - `feat/routing-capacity-score`
   - `fix/billing-reconciliation`
   - `docs/patient-flow-methodology`
   - `test/routing-edge-cases`
3. Make the smallest coherent change that solves the issue.
4. Run relevant notebooks, tests, validation scripts, or checks locally where applicable.
5. Update documentation, manifest counts, or provenance notes when your change affects them.
6. Commit using a Conventional Commit-style message, for example `feat(routing): add capacity-aware scoring`.
7. Open a pull request to `main` and explain what changed, why it changed, how it was validated, and any limitations.

## Pull request checklist

- [ ] The change has a clear purpose and scoped implementation.
- [ ] No real patient, biometric, credential, financial, or sensitive personal data is included.
- [ ] Synthetic-data provenance remains clear.
- [ ] Clinical and operational responsibilities are not conflated.
- [ ] Relevant notebooks/scripts/tests were run or the reason they were not run is documented.
- [ ] Documentation is updated when behaviour, data, architecture, or assumptions change.
- [ ] New dependencies are necessary and documented.
- [ ] Generated outputs or large files are included only when they add clear project value.
- [ ] The contribution follows `SECURITY.md`, `CODE_OF_CONDUCT.md`, and applicable license terms.

## Data changes

When adding or changing synthetic datasets:

- preserve schema consistency unless the change intentionally updates the schema;
- document generation logic or source assumptions;
- avoid values copied from identifiable real patients;
- update `MANIFEST.json` when canonical row or record counts change; and
- update provenance or usage documentation when the data-generation approach changes.

## Analytics and model changes

For KPI, financial, workforce, routing, queue, or predictive-model changes, include enough information for another contributor to understand:

- the decision question;
- the variables or features used;
- the calculation or model logic;
- evaluation or validation method;
- known limitations; and
- how the output should and should not be interpreted.

## Documentation changes

Documentation improvements are welcome, especially when they make the patient journey, HR Operations implications, routing logic, billing model, data provenance, or governance controls easier to understand.

## Security or privacy concerns

Do not open a public issue containing secrets, real patient data, private identifiers, or exploitable sensitive details. Follow `SECURITY.md` and use an appropriate private reporting path to the maintainer.

## License

By contributing, you agree that your contribution may be distributed under the repository's applicable license terms.
