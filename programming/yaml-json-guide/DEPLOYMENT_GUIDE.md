---
title: Jekyll Deployment Guide
description: Complete guide to deploying markdown documentation with Jekyll on GitHub Pages
layout: default
---

# Jekyll Deployment Guide: Markdown to HTML with Mermaid & TOC Links

**Purpose:** This guide documents how we successfully deployed the YAML & JSON Guide to GitHub Pages using Jekyll, including solutions for Mermaid diagram rendering and Table of Contents navigation.

**Use Case:** Reference for future Jekyll deployments with complex markdown features (diagrams, internal links, custom styling).

---

## 📚 Table of Contents

1. [Overview](#overview)
2. [Jekyll Configuration](#jekyll-configuration)
3. [Markdown to HTML Conversion](#markdown-to-html-conversion)
4. [Mermaid Diagram Rendering](#mermaid-diagram-rendering)
5. [Table of Contents Anchor Links](#table-of-contents-anchor-links)
6. [Custom Layout Setup](#custom-layout-setup)
7. [Deployment Workflow](#deployment-workflow)
8. [Troubleshooting](#troubleshooting)

---

<a id="overview"></a>
## 1. Overview

### The Challenge

We needed to deploy a large markdown documentation repository (7,600+ lines, 14 Mermaid diagrams, extensive Table of Contents) to GitHub Pages with:
- ✅ Clean HTML rendering from markdown files
- ✅ Working Mermaid diagram visualization
- ✅ Functional internal navigation (TOC links)
- ✅ Custom styling and layout
- ✅ No build process required (GitHub Pages handles it)

### The Solution

**Jekyll** - GitHub Pages' built-in static site generator that:
- Automatically converts `.md` files to `.html`
- Processes markdown with Kramdown (GitHub Flavored Markdown)
- Supports custom layouts and styling
- Deploys automatically on `git push`

---

<a id="jekyll-configuration"></a>
## 2. Jekyll Configuration

### Repository Structure

```
documentation/
├── _config.yml              # Jekyll configuration (root level)
├── _layouts/
│   └── default.html         # Custom layout for markdown files
├── programming/
│   └── yaml-json-guide/
│       ├── index.html       # Landing page
│       ├── YAML_and_JSON_Guide.md
│       ├── USER_GUIDE.md
│       └── YAML_JSON_Cheat_Sheet.md
```

### _config.yml Setup

**Location:** `D:/github_upload/documentation/_config.yml`

```yaml
# Documentation Repository - Jekyll Configuration

# Site Settings
title: Technical Documentation Collection
description: Programming guides, system administration, and development resources
author: Ahmed Abdelhaleem
url: https://abdelhaleemahmed.github.io
baseurl: /documentation

# Build Settings
markdown: kramdown
kramdown:
  input: GFM                    # GitHub Flavored Markdown
  auto_ids: true                # Enable automatic ID generation
  parse_block_html: true        # Parse HTML blocks
  syntax_highlighter: rouge     # Code syntax highlighting
  syntax_highlighter_opts:
    css_class: 'highlight'

# Plugins (GitHub Pages safe plugins)
plugins:
  - jekyll-relative-links       # Convert relative links
  - jekyll-optional-front-matter # Allow markdown without front matter
  - jekyll-titles-from-headings # Generate titles from first heading

# Plugin Configuration
relative_links:
  enabled: true
  collections: false

optional_front_matter:
  remove_originals: false

titles_from_headings:
  enabled: true
  strip_title: true
  collections: false

# File Handling
include:
  - README.md

exclude:
  - node_modules/
  - vendor/
  - .git/
  - .gitignore
```

**Key Settings Explained:**

- **`markdown: kramdown`** - Use Kramdown parser (required for GitHub Pages)
- **`input: GFM`** - Use GitHub Flavored Markdown syntax
- **`auto_ids: true`** - CRITICAL: Enables custom anchor IDs (but see gotcha below)
- **`parse_block_html: true`** - Allows HTML within markdown
- **`baseurl: /documentation`** - Sets the base URL for the site

---

<a id="markdown-to-html-conversion"></a>
## 3. Markdown to HTML Conversion

### How Jekyll Converts .md to .html

**Step 1: Front Matter**

Every markdown file needs front matter at the top:

```markdown
---
title: Your Page Title
description: Page description
layout: default
---

# Your Content Here
```

**Step 2: Jekyll Processing**

1. Jekyll reads `.md` files
2. Extracts front matter (YAML between `---`)
3. Processes markdown with Kramdown
4. Applies the specified layout (`default.html`)
5. Generates `.html` file with same name

**Step 3: URL Structure**

```
Source:    programming/yaml-json-guide/YAML_and_JSON_Guide.md
Output:    programming/yaml-json-guide/YAML_and_JSON_Guide.html
Live URL:  https://abdelhaleemahmed.github.io/documentation/programming/yaml-json-guide/YAML_and_JSON_Guide.html
```

### Linking Between Files

**In index.html:**
```html
<!-- Link to markdown file (Jekyll converts to .html) -->
<a href="YAML_and_JSON_Guide.html">Read the Guide</a>
<a href="USER_GUIDE.html">User Guide</a>
```

**IMPORTANT:** Links must use `.html` extension, NOT `.md`, because Jekyll serves the converted HTML files.

---

<a id="mermaid-diagram-rendering"></a>
## 4. Mermaid Diagram Rendering

### The Problem

**Markdown Source:**
```markdown
​```mermaid
graph TD
    A[Start] --> B[End]
​```
```

**Jekyll Output:**
```html
<pre><code class="language-mermaid">
graph TD
    A[Start] --> B[End]
</code></pre>
```

**Mermaid.js Expects:**
```html
<div class="mermaid">
graph TD
    A[Start] --> B[End]
</div>
```

**Result:** Diagrams displayed as code blocks instead of rendered graphics.

### The Solution

Created a JavaScript function in the layout to convert Jekyll's code blocks to Mermaid divs:

**Location:** `_layouts/default.html`

```html
<!-- Mermaid.js for diagram rendering -->
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<script>
    // Initialize Mermaid
    mermaid.initialize({
        startOnLoad: false,
        theme: 'default',
        securityLevel: 'loose',
        flowchart: {
            useMaxWidth: true,
            htmlLabels: true,
            curve: 'basis'
        }
    });

    // Convert Jekyll's <code class="language-mermaid"> to renderable Mermaid diagrams
    document.addEventListener('DOMContentLoaded', function() {
        // Find all code blocks with language-mermaid class
        const mermaidBlocks = document.querySelectorAll('code.language-mermaid');

        mermaidBlocks.forEach((block, index) => {
            // Create a new div with mermaid class
            const mermaidDiv = document.createElement('div');
            mermaidDiv.className = 'mermaid';
            mermaidDiv.textContent = block.textContent;

            // Replace the pre>code block with the mermaid div
            const preBlock = block.parentElement;
            preBlock.parentElement.replaceChild(mermaidDiv, preBlock);
        });

        // Now render all mermaid diagrams
        mermaid.run();
    });
</script>
```

**How It Works:**

1. **Page loads** → JavaScript waits for DOM ready
2. **Find blocks** → Searches for all `code.language-mermaid` elements
3. **Convert** → Creates `<div class="mermaid">` with the code content
4. **Replace** → Swaps the code block with the div
5. **Render** → Calls `mermaid.run()` to visualize all diagrams

**Result:** All 14 Mermaid diagrams render as interactive SVG graphics.

---

<a id="table-of-contents-anchor-links"></a>
## 5. Table of Contents Anchor Links

### The Problem

**Table of Contents in Markdown:**
```markdown
1. [Introduction & History](#1--introduction--history)
2. [Quick Comparison](#2--quick-comparison-yaml-vs-json)
3. [YAML Deep Dive](#3--yaml-deep-dive)
```

**Initial Attempt (FAILED):**

Used Kramdown's `{#id}` syntax:
```markdown
## 1. 📜 Introduction & History 🟢 {#1--introduction--history}
```

**Problem:** GitHub Pages GFM doesn't support Kramdown's `{#id}` syntax. The `{#1--introduction--history}` appeared as **literal text** in the heading instead of being processed as an anchor ID.

### The Solution

Use **HTML anchors** directly in markdown (universally supported):

```markdown
<a id="1--introduction--history"></a>
## 1. 📜 Introduction & History 🟢

<a id="2--quick-comparison-yaml-vs-json"></a>
## 2. ⚖️ Quick Comparison: YAML vs JSON 🟢

<a id="3--yaml-deep-dive"></a>
## 3. 🧭 YAML Deep Dive 🟢🟡
```

**Why This Works:**

- HTML anchors (`<a id="...">`) work in **all** markdown processors
- GFM, Kramdown, CommonMark all preserve HTML tags
- No special configuration needed
- Headings display clean (no `{#id}` text)

**Implementation:**

Used Python script to convert all headings:

```python
import re

with open('YAML_and_JSON_Guide.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace {#id} syntax with HTML anchors
replacements = [
    (r'^(## 1\. 📜 Introduction & History 🟢) \{#1--introduction--history\}$',
     r'<a id="1--introduction--history"></a>\n\1'),
    (r'^(## 2\. ⚖️ Quick Comparison: YAML vs JSON 🟢) \{#2--quick-comparison-yaml-vs-json\}$',
     r'<a id="2--quick-comparison-yaml-vs-json"></a>\n\1'),
    # ... more replacements
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

with open('YAML_and_JSON_Guide.md', 'w', encoding='utf-8') as f:
    f.write(content)
```

**Result:** All Table of Contents links work perfectly.

---

<a id="custom-layout-setup"></a>
## 6. Custom Layout Setup

### Layout File Structure

**Location:** `_layouts/default.html`

**Purpose:** Provides consistent HTML structure, styling, and JavaScript for all markdown files.

**Complete Layout:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page.title | default: site.title }}</title>
    <meta name="description" content="{{ page.description | default: site.description }}">

    <style>
        /* GitHub-style markdown CSS */
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 980px;
            margin: 0 auto;
            padding: 2rem;
            background: #fff;
        }

        h1, h2, h3, h4, h5, h6 {
            margin-top: 1.5rem;
            margin-bottom: 1rem;
            font-weight: 600;
            line-height: 1.25;
        }

        h1 { font-size: 2rem; border-bottom: 1px solid #eaecef; padding-bottom: 0.3rem; }
        h2 { font-size: 1.5rem; border-bottom: 1px solid #eaecef; padding-bottom: 0.3rem; }
        h3 { font-size: 1.25rem; }
        h4 { font-size: 1rem; }

        code {
            background: #f6f8fa;
            padding: 0.2em 0.4em;
            border-radius: 3px;
            font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
            font-size: 85%;
        }

        pre {
            background: #f6f8fa;
            padding: 16px;
            overflow: auto;
            border-radius: 6px;
            line-height: 1.45;
        }

        pre code {
            background: transparent;
            padding: 0;
        }

        /* Mermaid diagram styling */
        .mermaid {
            text-align: center;
            margin: 1em 0;
        }

        /* Back to top button */
        .back-to-top {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: #0366d6;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            text-decoration: none;
            display: none;
        }

        .back-to-top:hover {
            background: #0256c7;
            text-decoration: none;
        }

        @media (max-width: 768px) {
            body {
                padding: 1rem;
            }
        }
    </style>
</head>
<body>
    <div class="content">
        {{ content }}
    </div>

    <a href="#" class="back-to-top" id="backToTop">↑ Top</a>

    <!-- Mermaid.js for diagram rendering -->
    <script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
    <script>
        // Mermaid initialization and conversion (see section 4)
        mermaid.initialize({
            startOnLoad: false,
            theme: 'default',
            securityLevel: 'loose',
            flowchart: {
                useMaxWidth: true,
                htmlLabels: true,
                curve: 'basis'
            }
        });

        document.addEventListener('DOMContentLoaded', function() {
            const mermaidBlocks = document.querySelectorAll('code.language-mermaid');
            mermaidBlocks.forEach((block, index) => {
                const mermaidDiv = document.createElement('div');
                mermaidDiv.className = 'mermaid';
                mermaidDiv.textContent = block.textContent;
                const preBlock = block.parentElement;
                preBlock.parentElement.replaceChild(mermaidDiv, preBlock);
            });
            mermaid.run();
        });
    </script>

    <!-- Back to top button functionality -->
    <script>
        window.addEventListener('scroll', function() {
            const backToTop = document.getElementById('backToTop');
            if (window.pageYOffset > 300) {
                backToTop.style.display = 'block';
            } else {
                backToTop.style.display = 'none';
            }
        });

        document.getElementById('backToTop').addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    </script>
</body>
</html>
```

**Jekyll Variables Used:**

- `{{ page.title }}` - From markdown front matter
- `{{ page.description }}` - From markdown front matter
- `{{ site.title }}` - From _config.yml
- `{{ content }}` - The processed markdown content

---

<a id="deployment-workflow"></a>
## 7. Deployment Workflow

### Step-by-Step Process

**1. Prepare Markdown Files**

Add front matter to all `.md` files:
```markdown
---
title: Page Title
description: Page description
layout: default
---
```

**2. Create Custom Layout**

Create `_layouts/default.html` with:
- GitHub-style CSS
- Mermaid.js integration
- Back-to-top button
- Responsive design

**3. Configure Jekyll**

Create `_config.yml` at repository root with:
- Kramdown settings
- Plugin configuration
- Site metadata

**4. Fix Anchor Links**

Add HTML anchors before all section headings:
```markdown
<a id="section-name"></a>
## Section Heading
```

**5. Update index.html Links**

Change all `.md` links to `.html`:
```html
<!-- Before -->
<a href="guide.md">Guide</a>

<!-- After -->
<a href="guide.html">Guide</a>
```

**6. Commit and Push**

```bash
cd D:/github_upload/documentation
git add -A
git commit -m "Setup Jekyll with Mermaid and TOC fixes"
git push origin main
```

**7. Wait for GitHub Pages**

- GitHub Pages automatically builds (1-2 minutes)
- Check build status: Repository → Settings → Pages
- View live site: `https://username.github.io/repository/`

**8. Verify**

- ✅ Landing page loads (index.html)
- ✅ Markdown files render as HTML
- ✅ TOC links navigate correctly
- ✅ Mermaid diagrams display as graphics
- ✅ Styling looks correct
- ✅ Mobile responsive

---

<a id="troubleshooting"></a>
## 8. Troubleshooting

### Common Issues and Solutions

#### Issue 1: Mermaid Diagrams Show as Code

**Symptom:** Diagrams display as text in code blocks

**Solution:** Check that:
1. Mermaid.js script is loaded in layout
2. Conversion script runs on DOMContentLoaded
3. `code.language-mermaid` selector matches Jekyll output
4. `mermaid.run()` is called after conversion

**Debug:**
```javascript
// Add console logging
console.log('Mermaid blocks found:', mermaidBlocks.length);
```

#### Issue 2: TOC Links Don't Work

**Symptom:** Clicking TOC links doesn't navigate

**Solution:**
1. Verify HTML anchors exist: View page source, search for `<a id="`
2. Check anchor ID matches TOC href exactly
3. Use HTML anchors, not `{#id}` syntax
4. Ensure no typos in IDs (case-sensitive)

**Debug:**
```javascript
// Check if anchor exists
console.log(document.getElementById('section-name'));
```

#### Issue 3: 404 on .md URLs

**Symptom:** Links to `.md` files give 404 errors

**Solution:** Update all links to use `.html` extension

**Find and replace:**
```bash
# Find .md links in HTML files
grep -r '\.md"' *.html

# Replace with .html
sed -i 's/\.md"/.html"/g' index.html
```

#### Issue 4: GitHub Pages Not Building

**Symptom:** Changes don't appear on live site

**Solution:**
1. Check Repository → Settings → Pages
2. Verify source branch is correct
3. Check for build errors in Actions tab
4. Ensure `_config.yml` is valid YAML
5. Wait 2-3 minutes for build to complete

**Debug:**
```bash
# Test Jekyll locally
gem install bundler jekyll
jekyll serve
# Visit http://localhost:4000
```

#### Issue 5: Custom Layout Not Applied

**Symptom:** Markdown renders without styling

**Solution:**
1. Verify `_layouts/default.html` exists
2. Check front matter has `layout: default`
3. Ensure layout file is in repository root's `_layouts/`
4. Rebuild GitHub Pages (push a small change)

#### Issue 6: Kramdown {#id} Showing as Text

**Symptom:** `{#section-id}` appears in headings

**Solution:**
- **Don't use** Kramdown `{#id}` syntax with GFM
- **Use** HTML anchors: `<a id="section-id"></a>`
- Remove all `{#id}` from headings
- Add HTML anchors on line before heading

---

## Summary

### What We Accomplished

✅ **Jekyll Configuration** - Set up Kramdown with GFM for GitHub Pages
✅ **Markdown → HTML** - Automatic conversion with custom styling
✅ **Mermaid Diagrams** - JavaScript conversion for 14 interactive diagrams
✅ **TOC Navigation** - HTML anchor links for seamless internal navigation
✅ **Custom Layout** - GitHub-style design with back-to-top button
✅ **Zero Build Process** - GitHub Pages handles everything automatically

### Key Takeaways

1. **Use HTML anchors for IDs** - More compatible than Kramdown `{#id}`
2. **Convert Mermaid code blocks** - Jekyll output needs JavaScript transformation
3. **Link to .html not .md** - Jekyll serves converted HTML files
4. **Test locally first** - Use `jekyll serve` before deploying
5. **Front matter required** - Every .md file needs YAML front matter

### File Checklist

- ✅ `_config.yml` - Jekyll configuration at repository root
- ✅ `_layouts/default.html` - Custom layout with Mermaid support
- ✅ Front matter in all `.md` files - Title, description, layout
- ✅ HTML anchors before headings - `<a id="..."></a>`
- ✅ `.html` links in index.html - Not `.md`

---

**Created:** 2025-12-28
**Repository:** https://github.com/abdelhaleemahmed/documentation
**Live Site:** https://abdelhaleemahmed.github.io/documentation/programming/yaml-json-guide/

**Author:** Ahmed Abdelhaleem
**Purpose:** Reference guide for future Jekyll deployments with complex markdown features
