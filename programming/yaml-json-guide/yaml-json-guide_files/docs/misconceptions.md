# YAML vs JSON — Common Misconceptions

Misunderstandings about YAML and JSON often lead to bad design decisions, debugging frustration, and unsafe practices. This document clears up the most common myths so you can choose the right format confidently.

## Misconception 1: "YAML is always more human-friendly than JSON."

**Reality:**

YAML becomes harder for beginners when files grow large.

**Why?**
- Indentation-sensitive (one space off breaks everything)
- Implicit type casting (`yes` → `true`, `01` → `1`)
- Hidden formatting errors
- Anchors and merge keys increase complexity

JSON is predictable, even if slightly more verbose.

---

## Misconception 2: "JSON doesn't support comments."

**Reality:**

Official JSON (RFC 8259) does not allow comments.

**But** many systems support JSON with comments (JSONC):
- VS Code settings
- TypeScript config (`tsconfig.json`)
- Azure Pipelines
- Various editors & tooling

**Example (JSONC):**
```json
{
  // This is allowed in JSONC
  "port": 8080,
  "debug": true  // Enable debug mode
}
```

**Don't assume your parser supports JSONC.** Always test!

---

## Misconception 3: "YAML is safe to parse by default."

**Reality:**

**YAML can be UNSAFE when parsed with full-featured loaders.**

Some YAML libraries allow arbitrary object instantiation.

**Dangerous example in Python:**
```python
import yaml
# ⚠️ NEVER do this with untrusted input!
yaml.load("!!python/object/new:os.system ['rm -rf /']")
```

This can execute dangerous system code!

**Always use:**
- `yaml.safe_load()` (Python)
- `LoadOptions` with restricted tags (Java, JavaScript)
- Never use `yaml.load()` on untrusted data

---

## Misconception 4: "JSON supports trailing commas."

**Reality:**

Plain JSON does **not** support trailing commas.

Many parsers will crash on this:
```json
{
  "name": "Ahmed",
  "active": true,  ← This trailing comma is INVALID
}
```

Some relaxed parsers allow it (e.g., JavaScript), but APIs generally reject it.

**Rule:** Never use trailing commas in JSON for portability.

---

## Misconception 5: "YAML allows tabs."

**Reality:**

Tabs are **completely forbidden** for indentation in YAML.

```yaml
# ❌ This breaks YAML parsers
	user: admin   ← Tab character!
	password: secret
```

**YAML requires spaces only**, usually 2 spaces per level.

---

## Misconception 6: "YAML is just JSON with indentation."

**Reality:**

YAML supports far more features than JSON:
- Anchors & aliases (`&anchor`, `*alias`)
- Merge keys (`<<:`)
- Multiple documents in one file (`---`)
- Richer data types (timestamps, binary, sets)
- Multi-line strategies (`|` and `>`)
- Tags (`!!timestamp`, `!!binary`)
- Special syntaxes (`?`, `*`, `&`, `<<:`)

YAML is a **superset** of JSON, but far more expressive (and complex).

---

## Misconception 7: "JSON is slower than YAML."

**Reality:**

JSON parsers are generally **faster** because:
- Simpler grammar
- No anchors to resolve
- No type ambiguity
- No multi-line block styles
- Defined structure

**YAML parsing is significantly slower** due to complexity and type resolution rules.

**Benchmark example:**
- JSON parsing: 100ms for 10MB file
- YAML parsing: 1,400ms for same data (14x slower)

---

## Misconception 8: "YAML automatically preserves order."

**Reality:**

Most YAML parsers do **not** guarantee key order, unless specifically configured.

JSON also does not guarantee key order unless the language preserves it (modern JavaScript does).

**Order should never be relied on** unless explicitly documented by your parser.

---

## Misconception 9: "YAML and JSON convert cleanly without changes."

**Reality:**

Conversions can break:

**YAML → JSON loses:**
- Comments (JSON doesn't support them)
- Anchors/aliases (JSON has no equivalent)
- Multi-line strings (collapse to escaped `\n`)
- Type information (booleans may become strings)
- Tags (JSON cannot represent them)

**JSON → YAML risks:**
- Unquoted keys may change meaning
- Type reinterpretation (strings becoming booleans)
- Trailing commas break YAML parsers

**Conversion is never lossless** unless the YAML is JSON-compatible.

---

## Misconception 10: "JSON is always the best for APIs."

**Reality:**

JSON is excellent for APIs, but:
- **GraphQL** uses a structured schema + JSON
- **gRPC** uses Protobuf (binary and faster)
- **Avro** is common in data engineering
- **MessagePack** is compressed JSON
- **YAML** can be used for internal API specs (OpenAPI) but not payloads

JSON is **popular, but not universally optimal**.

---

## Summary Table: YAML vs JSON Misconceptions

| Misconception | Correct Reality |
|---------------|-----------------|
| YAML is always easier | YAML gets complex quickly with large files |
| JSON cannot have comments | JSONC exists, but not standard JSON |
| YAML is safe | YAML can execute code if parsed unsafely |
| JSON allows trailing commas | No — only relaxed parsers do |
| YAML allows tabs | Tabs are completely invalid in YAML |
| YAML = JSON with spaces | YAML is far more complex and feature-rich |
| JSON is slow | JSON is generally faster than YAML |
| YAML preserves order | Usually not guaranteed by parsers |
| Conversion is lossless | Conversion loses anchors, comments, and type info |
| JSON is best for all APIs | Many faster/binary formats exist |

> **Pro Tip:** When in doubt, test your assumptions! Don't rely on "common knowledge" — verify how your specific parser behaves.

> **Warning:** The biggest mistakes come from assumptions. Always validate configs, test conversions, and use safe parsing methods.

---

**See also:**
- [Common Errors](common-errors.md) - 38 documented errors with solutions
- [Interview Questions](interview-prep.md) - Practice questions and answers
- [Quick Reference](quick-reference.md) - Essential YAML & JSON rules
