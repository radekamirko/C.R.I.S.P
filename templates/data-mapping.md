# Data Mapping

**Project:**
**Feature:**
**Date:**

---

> Use this template whenever a feature involves extracting, transforming, or mapping structured data.
> Examples: OCR from documents, API response parsing, CSV/Excel imports, form submissions to DB, webhook payloads.
>
> If the mapping isn't defined before the sprint starts, Claude will guess. It will be wrong.

---

## Source Description

**What is the data source?**
_(PDF document, API response, CSV, form, webhook payload, etc.)_


**How is it accessed?**
_(File upload, API call, scheduled pull, user input, etc.)_


**Sample available?**
- [ ] Yes — attach or describe below
- [ ] No — describe expected structure

**Sample / structure description:**
```
(paste sample here — redact any real PII)
```

---

## Document / Response Structure

> For each section of the source, describe what's in it and where to find it.

| Section / Area | Location in source | Description | Example value |
|---|---|---|---|
| | Page __, section __ / JSON path / column | | |
| | | | |
| | | | |

**Navigation notes:**
_(How to identify sections, headers, repeating rows, nested objects, etc.)_


---

## Field-by-Field Mapping

> Map every extracted field to its destination. Be explicit — field names, types, DB columns.

| Source field | Location in source | Target DB table | Target column | Data type | Transformation required |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

**Transformation notes:**
_(Date format conversions, string cleaning, unit changes, concatenation, splitting, etc.)_


---

## Edge Cases & Nulls

> What happens when a field is missing, malformed, or unexpected?

| Field | Edge case | Behaviour |
|---|---|---|
| | Missing / blank | Fail? Default value? Skip record? |
| | Malformed / wrong format | |
| | Multiple values where one expected | |
| | Value outside expected range | |

**Global rules for missing data:**
- [ ] Fail hard — reject the entire record and alert
- [ ] Fail soft — skip the field, log a warning, continue
- [ ] Use default: _(specify default values)_


---

## Validation Rules

> What must be true before a record is saved?

| Field | Validation rule | Error behaviour |
|---|---|---|
| | Required / not null | |
| | Must match format (regex, enum) | |
| | Must be unique | |
| | Must exist in another table (FK) | |

**Post-extraction validation:**
- [ ] Run validation before DB write — reject invalid records
- [ ] Log all rejected records with reason
- [ ] Alert if rejection rate exceeds ___%


---

## Output / Confirmation

**What happens after successful extraction and save?**
_(e.g. record created in DB, user notified, downstream job triggered)_


**What does failure look like to the user?**
_(Error message, retry option, fallback)_


---

## Open Questions

> Every question here must be answered before the sprint that uses this mapping starts.

- [ ]
- [ ]
- [ ]
