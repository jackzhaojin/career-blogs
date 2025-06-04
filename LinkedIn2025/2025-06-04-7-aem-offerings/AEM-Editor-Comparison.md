## AEM Editor Comparison – Insights and Summary

This canvas collects key points to support future discussions around Adobe Experience Manager (AEM) editor choices, particularly comparing Universal Editor (UE) with traditional Sites Editor and Content Fragment Editor (CFE).

---

### ✅ Slide Summary Validation (from Adobe)

#### Content Fragment Editor

| **Claim**           | **Accuracy**                                                                     |
| ------------------- | -------------------------------------------------------------------------------- |
| Built into AEM      | ✅ Accurate                                                                       |
| Form-based          | ✅ Accurate                                                                       |
| Decoupled from UI   | ✅ Accurate                                                                       |
| Focused on Headless | ✅ Accurate. Schema-based, UI-agnostic, primarily used with GraphQL or JSON APIs. |

#### Sites Editor

| **Claim**                        | **Accuracy**                                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------------ |
| Built into AEM                   | ✅ Accurate                                                                                 |
| Page-based                       | ✅ Accurate                                                                                 |
| WYSIWYG and inline editing       | ✅ Accurate                                                                                 |
| Tightly coupled to AEM rendering | ✅ Accurate                                                                                 |
| Focus on headful implementations | ✅ Accurate                                                                                 |
| Complex for headless             | ✅ Accurate. Editable templates and HTL require `.model.json` configs for headless support. |

#### Universal Editor

| **Claim**                                                  | **Accuracy**                                                               |
| ---------------------------------------------------------- | -------------------------------------------------------------------------- |
| Separate from AEM                                          | ✅ Accurate                                                                 |
| Inline editing for both Sites and Content Fragment content | ✅ Accurate                                                                 |
| Support for any backend through extensions                 | ✅ Mostly accurate. Requires dev setup via SDK/extensions.                  |
| Support for Edge Delivery Services (EDS)                   | ✅ Accurate                                                                 |
| Simple integration approach                                | ✅ Accurate. Lightweight integration especially with EDS and external SPAs. |

---

### 💡 When to Use Universal Editor

UE is less feature-rich than Sites Editor (no editable templates, weaker dialog support), but it's preferable in the following scenarios:

* **Headless/Hybrid Architectures**: React/Next.js frontends consuming content via APIs.
* **Edge Delivery Services**: Optimized for stateless, fast-delivery HTML sites.
* **Multi-channel Reuse**: Content fragments reused across web, mobile, and kiosk.
* **Developer-controlled Frontends**: Rendering logic lives outside AEM (e.g., external JS apps).

---

### 🔄 Why Traditional Sites Editor May Be Preferred

Use Sites Editor when:

* You want drag-and-drop layout control.
* You use editable templates and policies.
* You're building headful AEM sites using HTL and Sling Models.
* You rely heavily on component dialogs and in-place authoring.

---

### 🤝 User Context Notes

* The user is a senior AEM architect familiar with Sites, EDS, and hybrid deployments.
* They’re comparing modern authoring strategies (UE vs Sites) for client use cases.
* They've noted that UE lacks editable templates and advanced dialogs.
* They are building both internal and client-facing narratives requiring Adobe alignment.
* They have live examples of Sites, Headless, and EDS-based deployments (e.g., newsroom.accenture.com).

---

Let me know if you'd like this formatted for slides, turned into an infographic, or extended into a client-facing matrix.
