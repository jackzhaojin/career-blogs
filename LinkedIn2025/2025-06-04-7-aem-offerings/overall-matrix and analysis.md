# AEM + EDS Capability Matrix and Observations

This document captures a consolidated understanding of Adobe Experience Manager (AEM) delivery models, with a focus on Edge Delivery Services (EDS), Universal Editor (UE), and document-based authoring approaches. It synthesizes client-facing configurations, backend architecture, and sample implementations, based on insights and discussions.

## 🧩 Delivery Model Matrix

| Configuration             | Sample Site                                                      | Glass / Client HTML    | AEM Store           | Authoring Method   | Editor         | How It Works                                     | Backend Dev        | Notes                    |
| ------------------------- | ---------------------------------------------------------------- | ---------------------- | ------------------- | ------------------ | -------------- | ------------------------------------------------ | ------------------ | ------------------------ |
| **Classic AEM 6.5**       | *Should not disclose*                                            | AEM Rendering Engine   | JCR (Sites/XF/CF)   | Touch UI           | Classic Editor | `/crx/de`, editable nodes                        | ✅ Full access      | Legacy setups            |
| **Classic AEMaaCS**       | [accenture.com](https://www.accenture.com)                       | AEM Rendering Engine   | JCR (Sites/XF/CF)   | Touch UI           | Classic Editor | Cloud containerized image from `/apps/libs`      | ✅ Full access      | Standard AEMaaCS setup   |
| **AEM w/ SPA SDKs**       | *Should not disclose*                                            | External (CSR/SSR)     | Pages               | Remote authored    | SPA App        | React SDK + markup pull                          | ⚠️ Limited         | Uses remote frontend     |
| **AEMaaCS Headless + UE** | *Should not disclose*                                            | External (CSR/SSR)     | CF Models + GraphQL | UE dialogs         | UE on CF       | Iframe editor + persisted queries                | ⚠️ CF only         | True headless            |
| **UE w/ AEM Sites**       | [ue-remote-app.adobe.net](https://ue-remote-app.adobe.net)       | External (.model.json) | Pages               | UE Dialogs         | UE             | Iframe + decorate                                | ⚠️ Simplified HTML | Model JSON-based editing |
| **AEM UE with EDS**       | [experienceleague.adobe.com](https://experienceleague.adobe.com) | EDS Runtime            | Pages               | UE Dialogs         | UE             | HTML rendered by AEM, decorated by `decorate.js` | ❌ No backend dev   | Static+Dynamic hybrid    |
| **Docs with EDS**         | [newsroom.accenture.com](https://newsroom.accenture.com)         | EDS Runtime            | GDocs/SharePoint    | Word / Google Docs | Sidekick / EDS | Doc → Markdown → HTML → decorate.js              | ❌ No backend dev   | Fastest to author        |

## 🔍 Additional Capability Highlights

* **Universal Editor (UE)** can be used with both Sites-based pages and document-generated content.
* **decorate.js** plays a critical role in EDS setups by transforming raw HTML (from AEM or Markdown) into block-decorated HTML.
* AEM developers author very **simple semantic HTML** when using EDS. Styling, layout, and interaction are handled by EDS boilerplate.
* In **AEM + EDS setups**, the HTML is rendered by AEM, not JSON — this is confirmed by Adobe’s own guidance.
* **Experience League** is a production-grade example of AEM UE + EDS, featuring high performance and document integration.

## 🔧 JSON & API Options in AEM

| Method                      | Content Source          | Use Case                         |
| --------------------------- | ----------------------- | -------------------------------- |
| Java Servlets               | Pages, XF, CF           | Legacy projects                  |
| `.model.json`               | Pages + Core Components | Sites + UE-compatible editing    |
| Content Fragment API        | Content Fragments       | Headless delivery for mobile/web |
| GraphQL + Persisted Queries | CF + Relationships      | Multi-level headless queries     |

## 📌 Observations

* EDS promotes a clean separation of concerns: content comes from AEM or Docs, but layout/rendering is handled at runtime.
* The authoring experience is streamlined through UE, regardless of whether the source is AEM or Google Docs.
* AEM projects using EDS benefit from simplified deployment and fewer backend concerns.
* Document-based authoring (Word/GDocs) is the fastest, most scalable authoring model, ideal for newsroom-like setups.

---

This matrix and overview are based on live references, project insights, and Adobe’s official documentation across Experience League, GitHub, and partner ecosystems like AmeXio Fuse.
