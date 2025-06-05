### AEM Offerings by Feature (Matrix View)

This document presents Adobe Experience Manager (AEM) product offerings as columns and key feature dimensions as rows, grouped into two perspectives:

- **Functional / Authoring / End User Experience**
- **Non-Functional / Technical / Infrastructure / Analytics**

---

#### 🧩 Functional, Authoring & End User Experience

Note: My employwer Accenture's own sites examples are used here, or Adobe references.

Second note: There is a lot of information here and some are up for debate, please post so I can learn and update this chart.

##### Traditional AEM Solutions

| Feature / Capability                            | Classic AEM 6.5 (Core Comp)       | AEMaaCS (Core Comp)                          | AEM w/ SPA SDKs         |
| ----------------------------------------------- | --------------------- | ------------------------------------------ | ----------------------- |
| **Sample Site**                                 | *Should be obvious* | [accenture.com](https://www.accenture.com) | *Should not disclose*   |
| **Authoring Mode**                              | Touch UI              | Touch UI                                   | Touch UI                |
| **Editor Used**                                 | Classic Dialog xml Editor        | Classic Dialog xml Editor                             | Classic Editor          |
| **DAM / Asset Usage**                           | AEM Assets            | AEM Assets (cloud-optimized)               | ✅                       |
| **Authoring Speed**                             | Slowest               | Faster                                     | Medium                  |
| **End User Personalization Experience**         | Adobe Target / AJO    | Same                         | Same                    |
| **Author Personalization Integration (Target)** | ✅ Experience Fragment                | ✅ Experience Fragment                                     | ⚠️ Depends |
| **Business Use Case Fit**                       | Full control, legacy  | Full stack CMS                             | SPA-heavy frontend, legacy      |

##### Modern/Headless AEM Solutions

| Feature / Capability                            | AEM Headless CF + UE  | UE with AEM Sites                                          | AEM UE + EDS                                                     | Docs with EDS                                            |
| ----------------------------------------------- | --------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------- |
| **Sample Site**                                 | *Should not disclose* | [ue-remote-app.adobe.net](https://ue-remote-app.adobe.net) | [experienceleague.adobe.com](https://experienceleague.adobe.com) | [newsroom.accenture.com](https://newsroom.accenture.com) |
| **Authoring Mode**                              | UE Dialogs (CFs)      | UE Dialogs (page + model def)                                               | UE Dialogs  (page + model def)                                                          | Word/Google Docs                                         |
| **Editor Used**                                 | Universal Editor      | Universal Editor                                           | Universal Editor                                                 | Docs Editor + Sidekick                                   |
| **DAM / Asset Usage**                           | AEM Assets (cloud-optimized)           | ✅                                                          | ✅                                                                | Optimized via EDS                                                        |
| **Authoring Speed**                             | Fast                  | Medium                                                       | Medium                                                          | Fastest                                                  |
| **End User Personalization Experience**         | Same                  | Same                                                       | Same                                         | Same                                                        |
| **Author Personalization Integration (Target)** | ✅ Content Fragment         | ✅ Exfrag                                                    | ⚠️ Actually not sure what OOTB support is here                                                | ❌      No productized content to Target offer export                                                   |
| **Business Use Case Fit**                       | API-first, modern, mobile/web | Modern Sites Authoring?                                     | High-performance Sites with AEM features (workflows, permissions, etc)                                          | Editorial /Newsrooms / Speed / Ease of Use                                      |


---

#### 🔧 Non-Functional, Technical, Infrastructure & Analytics

##### Traditional AEM Solutions

| Feature / Capability         | Classic AEM 6.5 (Core Comp)              | AEMaaCS (Core Comp)            | AEM w/ SPA SDKs               |
|-----------------------------|-------------------------------|------------------------------|-------------------------------|
| **Client HTML Rendering**   | AEM Renderer                  | AEM Renderer                 | External (CSR/SSR)            |
| **Backend Dev in AEM**      | ✅ Full                        | ✅ Full                      | ✅ (limited to content)        |
| **Content Stored In**       | JCR (Sites/XF/CF)             | JCR (Sites/XF/CF)            | Pages                         |
| **Delivery Architecture**   | Monolithic / Dispatcher       | Cloud Containerized          | Headless App + AEM APIs                |
| **Analytics Support**       | Adobe Analytics via Datalayer | Same                         | ⚠️ Varies (depends on SPA)       |
| **Technical Use Case**      | Full-stack, high control      | Scalable enterprise CMS      | Decoupled UI, app-driven      |
| **Ways to Get Markdown / JSON**        | `.model.json`                | `.model.json`                | `.model.json`                 |

##### Modern/Headless AEM Solutions

| Feature / Capability         | AEM Headless CF + UE          | UE with AEM Sites                 | AEM UE + EDS                   | Docs with EDS                        |
|-----------------------------|-------------------------------|----------------------------------|-------------------------------|------------------------------------|
| **Client HTML Rendering**   | External (CSR/SSR)            | AEM-rendered HTML enhanced via .model.json endpoints (i could make this blog 8 capabilities)                     | EDS Runtime                   | EDS Runtime                        |
| **Backend Dev in AEM**      | ⚠️ Not recommended             | ✅ Full                    | ❌                             | ❌                                  |
| **Content Stored In**       | Content Fragments                     | Pages                            | Pages                         | Docs (GDocs/SharePoint)            |
| **Delivery Architecture**   | Headless App + Headless API          | Headless App + AEM Sites Headless API. Or just AEM Sites            | AEM Sites + decorate.js      | Markdown → HTML + decorate.js      |
| **Analytics Support**       |⚠️ Varies (depends on SPA)          | Depends on HTML or JSON             | ⚠️ Varies (depends on impl)      | ⚠️ Varies (depends on impl) |
| **Technical Use Case**      | Pure headless delivery        | Editable sites with .model.json. Or extend on typcial sites but not use dialogs. | Edge-performant hybrid       | Doc-driven publishing with no CMS  |
| **Ways to Get Markdown / JSON**        | GraphQL + Persisted Query          | `.model.json`    .infinity.json                 | .md                              | .md                                   |

---
