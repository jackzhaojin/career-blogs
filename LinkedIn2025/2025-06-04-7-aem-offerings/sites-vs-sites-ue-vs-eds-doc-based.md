# 🧭 AEM Authoring Models Comparison and Client Readiness Notes

## 💡 Summary of Key AEM Authoring Models

This canvas summarizes the differences between three main AEM authoring approaches, with a focus on headless readiness, functional trade-offs, and client fit.

### 1. AEM 6.5 Sites (Classic WCM)

* **Authoring:** Full-page WYSIWYG inside AEM using editable templates and drag-and-drop components
* **Rendering:** HTML rendered server-side by AEM
* **Layout Control:** Authors manage layout using editable templates
* **Developer Involvement:** Low once templates are built
* **Content Reuse:** Limited across channels; primarily for websites
* **Target Use Case:** Traditional enterprise websites with full AEM stack

### 2. AEM Sites + Universal Editor (UE) – Headless

* **Authoring:** In-context editing on the real site (e.g., React/Next.js), enabled by UE instrumentation
* **Rendering:** Done on the frontend app (not AEM)
* **Layout Control:** Developers fully manage layout via frontend code
* **Developer Involvement:** High (must instrument site, define models, expose `.model.json` endpoints)
* **Content Reuse:** High (clean JSON APIs support omnichannel)
* **Target Use Case:** Enterprise headless setups with frontend flexibility but still needing visual authoring

### 3. Adobe Edge Delivery Services (EDS – Document-Based)

* **Authoring:** Structured documents in Google Docs or Word
* **Rendering:** Serverless HTML generation via Edge Runtime
* **Layout Control:** Fixed templates defined by developers (no editable templates)
* **Developer Involvement:** Medium (initial setup, templating, edge configuration)
* **Content Reuse:** Low to Medium (web-focused HTML; limited omnichannel)
* **Target Use Case:** High-speed publishing for campaign or newsroom sites

## ✅ Validated Observations

* **EDS lacks editable templates** — layout is fixed by developer-defined boilerplate
* **EDS is web-first only** — JSON reuse across mobile, email, IoT is limited
* **EDS developer effort is medium** — developers build the templating and delivery logic, but not deep component systems

## 📊 Final Functional Comparison Table

| Feature / Area                    | AEM 6.5 Sites                   | AEM Sites + UE (Headless)                | Adobe Edge Delivery Services (EDS)        |
| --------------------------------- | ------------------------------- | ---------------------------------------- | ----------------------------------------- |
| **Authoring Location**            | In AEM                          | On live site via UE overlay              | Google Docs or Word                       |
| **Rendering Responsibility**      | AEM                             | Frontend App (e.g., React)               | Edge Runtime                              |
| **Authoring Experience**          | WYSIWYG drag-and-drop           | In-context visual editing on real site   | Familiar doc-based with structure rules   |
| **Layout Control**                | Editable templates by authors   | Layout fixed by frontend devs            | Layout fixed by devs                      |
| **Content Reuse Across Channels** | Low                             | High (via `.model.json`)                 | Low to Medium                             |
| **Developer Involvement**         | Low after setup                 | High (modeling, instrumentation, APIs)   | Medium (templating, style logic)          |
| **Target Use Case**               | Traditional enterprise websites | Headless web with authoring control      | Speed-focused sites (newsroom, campaigns) |
| **Personalization**               | Supported                       | Supported with effort                    | Basic personalization support             |
| **Speed to Publish**              | Moderate                        | Moderate (depends on frontend readiness) | Very fast (Docs → live in minutes)        |
| **Omnichannel Support**           | Weak                            | Strong                                   | Weak                                      |

## 🎯 Client Notes

* Client is interested in **UE with Sites** — useful middle-ground for headless with visual editing
* Client is unclear about migration path from **AEM 6.5**:

  * **Content** can likely be migrated (structured pages)
  * **Components** must be rebuilt (new model, rendering, authoring configs)
  * **Authoring flow** shifts from inside AEM to editing on the live site
* Important to set expectations on **dev effort and authoring behavior changes**

Let me know if you’d like a visual slide, stakeholder-friendly doc, or technical deep dive added to this.
