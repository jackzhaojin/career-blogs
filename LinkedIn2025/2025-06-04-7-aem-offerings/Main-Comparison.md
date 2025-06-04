# AEM Offerings by Feature (Matrix View)

This document presents Adobe Experience Manager (AEM) product offerings as columns and key feature dimensions as rows, grouped into two perspectives:

- **Functional / Authoring / End User Experience**
- **Non-Functional / Technical / Infrastructure / Analytics**

---

## 🧩 Functional, Authoring & End User Experience

| Feature / Capability                            | Classic AEM 6.5       | AEMaaCS (Classic)                          | AEM w/ SPA SDKs         | AEM Headless CF + UE  | UE with AEM Sites                                          | AEM UE + EDS                                                     | Docs with EDS                                            |
| ----------------------------------------------- | --------------------- | ------------------------------------------ | ----------------------- | --------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------- |
| **Sample Site**                                 | *Should not disclose* | [accenture.com](https://www.accenture.com) | *Should not disclose*   | *Should not disclose* | [ue-remote-app.adobe.net](https://ue-remote-app.adobe.net) | [experienceleague.adobe.com](https://experienceleague.adobe.com) | [newsroom.accenture.com](https://newsroom.accenture.com) |
| **Authoring Mode**                              | Touch UI              | Touch UI                                   | Touch UI                | UE Dialogs (CFs)      | UE Dialogs                                                 | UE Dialogs                                                       | Word/Google Docs                                         |
| **Editor Used**                                 | Classic Editor        | Classic Editor                             | Classic Editor          | Universal Editor      | Universal Editor                                           | Universal Editor                                                 | Docs Editor + Sidekick                                   |
| **DAM / Asset Usage**                           | AEM Assets            | AEM Assets (cloud-optimized)               | ✅                       | ⚠️ Optional           | ✅                                                          | ✅                                                                | ❌                                                        |
| **Authoring Speed**                             | Slowest               | Faster                                     | Medium                  | Fast                  | Fast                                                       | Fastest                                                          | Fastest                                                  |
| **End User Personalization Experience**         | Adobe Target / AJO    | Adobe Target / AJO                         | Same                    | Same                  | Same                                                       | UE-aware personalization                                         | ❌                                                        |
| **Author Personalization Integration (Target)** | ✅ Full                | ✅ Full                                     | ⚠️ Integration required | ⚠️ Limited            | ✅ Supported                                                | ✅ UE-aware                                                       | ❌                                                        |
| **Business Use Case Fit**                       | Full control, legacy  | Full stack CMS                             | SPA-heavy frontend      | API-first, mobile/web | Modern Sites Authoring                                     | High-performance Sites                                           | Editorial/Newsrooms                                      |

---

## 🔧 Non-Functional, Technical, Infrastructure & Analytics

| Feature / Capability         | Classic AEM 6.5               | AEMaaCS (Classic)            | AEM w/ SPA SDKs               | AEM Headless CF + UE          | UE with AEM Sites                 | AEM UE + EDS                   | Docs with EDS                        |
|-----------------------------|-------------------------------|------------------------------|-------------------------------|-------------------------------|----------------------------------|-------------------------------|------------------------------------|
| **Client HTML Rendering**   | AEM Renderer                  | AEM Renderer                 | External (CSR/SSR)            | External (CSR/SSR)            | .model.json                      | EDS Runtime                   | EDS Runtime                        |
| **Backend Dev in AEM**      | ✅ Full                        | ✅ Full                      | ✅ (limited to content)        | ⚠️ Not recommended             | ⚠️ Partial                       | ❌                             | ❌                                  |
| **Content Stored In**       | JCR (Sites/XF/CF)             | JCR (Sites/XF/CF)            | Pages                         | CF Models                      | Pages                            | Pages                         | Docs (GDocs/SharePoint)            |
| **Delivery Architecture**   | Monolithic / Dispatcher       | Cloud Containerized          | SPA + AEM APIs                | Headless API + UE             | AEM Sites + decorate.js          | AEM Sites + decorate.js      | Markdown → HTML + decorate.js      |
| **Analytics Support**       | Adobe Analytics via Datalayer | Same                         | Varies (depends on SPA)       | Core Datalayer (CF)           | UE-aware Datalayer               | Datalayer + decorate.js      | Static tags (manual or build-time) |
| **Technical Use Case**      | Full-stack, high control      | Scalable enterprise CMS      | Decoupled UI, app-driven      | Pure headless delivery        | Editable sites with .model.json | Edge-performant hybrid       | Doc-driven publishing with no CMS  |
| **Ways to Get JSON**        | Custom Servlet                | `.model.json`                | `.model.json`                 | GraphQL + Persisted           | `.model.json`                    | ❌                             | ❌                                  |

---
