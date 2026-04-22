# Integration Map

**Project:** 
**Date:** 
**Mapped by:** 

---

> Every external system this product touches — what it provides, what it receives, how, and in what format.
> Fill this during Phase I. It becomes the source of truth for integration specs in Phase S.

---

## External Systems

| System name | Direction | Trigger | Data provided to us | Data we send to it | Format | Auth method | Notes |
|---|---|---|---|---|---|---|---|
| | Inbound / Outbound / Both | Event / Webhook / Schedule / Manual / API call | | | JSON / CSV / Webhook / Form / Other | API key / OAuth / Basic / None | |
| | | | | | | | |
| | | | | | | | |

---

## Integration Details

> For each system above, fill one section below.

---

### [System Name]

**What it does for this project:**

**Direction:** Inbound / Outbound / Both

**Trigger:**
_(What causes data to move? e.g. "user submits form", "new reply received in HeyReach campaign", "daily 9am schedule")_

**Data provided to us:**
_(Exact fields, structure — get a real example payload if possible)_
```
{
  "field": "value"
}
```

**Data we send to it:**
_(Exact fields we write or POST)_

**Format:** JSON / CSV / Webhook payload / REST API / Other

**Auth:** API key / OAuth2 / Basic auth / None

**Sandbox / test environment available?** Yes / No

**Known limitations or gotchas:**

**Sprint dependency:** _(which sprint first touches this integration)_

---

## Integration Dependencies

> Which features depend on which integrations? List here to inform sprint sequencing in Phase S.

| Feature | Depends on integration | Notes |
|---|---|---|
| | | |
| | | |

---

## Open Questions

_(Fill as you go — these must be resolved before Phase S integration specs are written)_

- [ ] 
- [ ] 
