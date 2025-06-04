Making Sense of 7 AEM Capabilities: Tradeoffs, Narratives, and Why It Matters

Before we dive in, this series of AEM blog posts will use fictitious language to protect my current and past clients. Instead of saying "we did this x times", I'll choose to say "it's possible to do this". For client protection, maybe from time to time, I might be making things up, but this should be rare.

This is my professional blog and does not represent Accenture's Adobe practice or our partnership with Adobe.

If you're interested in a deeper dive, stay tuned for upcoming blog entries that will go further into Universal Editor (UE) and Edge Delivery Services (EDS). Each of those deserves its own post.

Part 1: What the Situation Could Be

When consulting companies go to market, we pick a few of these to bring to customers. Some because the customer asked for it. At best, we take what we think is best for our customers. At worst, we focus on what we can execute on.

All of these options will not make it to any one single sales slide, I would imagine, from Adobe or any consulting firm. Capturing opportunities is about storytelling and narrative building. This slide, if shown out of context, will distract and confuse.

If Adobe had a workshop and decided EDS, service providers will bring EDS stories. If a long-time consulting team decided on headless CMS, then headless CMS will be the focus of storytelling from Adobe.

At best, consulting firms have the breadth to bring the best solution to the client. Leaner Adobe consulting partners may have to bring what they know or what they have staffing for.

To me, the big picture of all Adobe offerings is often lost in the process. However, seeing this landscape helps my technical brain. And hopefully, it’ll help you as well, without reading a 20 page readout.

Part 2: Approach and Implementation Journey

AEM Offerings by Feature (Matrix View)

This document presents Adobe Experience Manager (AEM) product offerings as columns and key feature dimensions as rows, grouped into two perspectives:

Functional / Authoring / End User Experience

information here and some are up for debate, please post so I can learn and update this chart.

| Feature / Capability                            | Classic AEM 6.5 (Core Comp)       | AEMaaCS (Core Comp)                          | AEM w/ SPA SDKs         | AEM Headless CF + UE  | UE with AEM Sites                                          | AEM UE + EDS                                                     | Docs with EDS                                            |
| ----------------------------------------------- | --------------------- | ------------------------------------------ | ----------------------- | --------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------- |
| **Sample Site**                                 | *Should be obvious* | [accenture.com](https://www.accenture.com) | *Should not disclose*   | *Should not disclose* | [ue-remote-app.adobe.net](https://ue-remote-app.adobe.net) | [experienceleague.adobe.com](https://experienceleague.adobe.com) | [newsroom.accenture.com](https://newsroom.accenture.com) |
| **Authoring Mode**                              | Touch UI              | Touch UI                                   | Touch UI                | UE Dialogs (CFs)      | UE Dialogs (page + model def)                                               | UE Dialogs  (page + model def)                                                          | Word/Google Docs                                         |
| **Editor Used**                                 | Classic Dialog xml Editor        | Classic Dialog xml Editor                             | Classic Editor          | Universal Editor      | Universal Editor                                           | Universal Editor                                                 | Docs Editor + Sidekick                                   |
| **DAM / Asset Usage**                           | AEM Assets            | AEM Assets (cloud-optimized)               | ✅                       | AEM Assets (cloud-optimized)           | ✅                                                          | ✅                                                                | Optimized via EDS                                                        |
| **Authoring Speed**                             | Slowest               | Faster                                     | Medium                  | Fast                  | Medium                                                       | Medium                                                          | Fastest                                                  |
| **End User Personalization Experience**         | Adobe Target / AJO    | Same                         | Same                    | Same                  | Same                                                       | Same                                         | Same                                                        |
| **Author Personalization Integration (Target)** | ✅ Experience Fragment                | ✅ Experience Fragment                                     | ⚠️ Depends | ✅ Content Fragment         | ✅ Exfrag                                                    | ⚠️ Actually not sure what OOTB support is here                                                | ❌      No productized content to Target offer export                                                   |
| **Business Use Case Fit**                       | Full control, legacy  | Full stack CMS                             | SPA-heavy frontend, legacy      | API-first, modern, mobile/web | Modern Sites Authoring?                                     | High-performance Sites with AEM features (workflows, permissions, etc)                                          | Editorial /Newsrooms / Speed / Ease of Use                                      |


Non-Functional / Technical / Infrastructure / Analytics


| Feature / Capability         | Classic AEM 6.5 (Core Comp)              | AEMaaCS (Core Comp)            | AEM w/ SPA SDKs               | AEM Headless CF + UE          | UE with AEM Sites                 | AEM UE + EDS                   | Docs with EDS                        |
|-----------------------------|-------------------------------|------------------------------|-------------------------------|-------------------------------|----------------------------------|-------------------------------|------------------------------------|
| **Client HTML Rendering**   | AEM Renderer                  | AEM Renderer                 | External (CSR/SSR)            | External (CSR/SSR)            | AEM-rendered HTML enhanced via .model.json endpoints (i could make this blog 8 capabilities)                     | EDS Runtime                   | EDS Runtime                        |
| **Backend Dev in AEM**      | ✅ Full                        | ✅ Full                      | ✅ (limited to content)        | ⚠️ Not recommended             | ✅ Full                    | ❌                             | ❌                                  |
| **Content Stored In**       | JCR (Sites/XF/CF)             | JCR (Sites/XF/CF)            | Pages                         | Content Fragments                     | Pages                            | Pages                         | Docs (GDocs/SharePoint)            |
| **Delivery Architecture**   | Monolithic / Dispatcher       | Cloud Containerized          | Headless App + AEM APIs                | Headless App + Headless API          | Headless App + AEM Sites Headless API. Or just AEM Sites            | AEM Sites + decorate.js      | Markdown → HTML + decorate.js      |
| **Analytics Support**       | Adobe Analytics via Datalayer | Same                         | ⚠️ Varies (depends on SPA)       |⚠️ Varies (depends on SPA)          | Depends on HTML or JSON             | ⚠️ Varies (depends on impl)      | ⚠️ Varies (depends on impl) |
| **Technical Use Case**      | Full-stack, high control      | Scalable enterprise CMS      | Decoupled UI, app-driven      | Pure headless delivery        | Editable sites with .model.json. Or extend on typcial sites but not use dialogs. | Edge-performant hybrid       | Doc-driven publishing with no CMS  |
| **Ways to Get JSON**        | Custom Servlet                | `.model.json`                | `.model.json`                 | GraphQL + Persisted           | `.model.json`    .infinity.json                 | ❌                             | ❌                                  |


These tables provide a snapshot of how the seven major AEM platform variations stack up. They range from traditional AEM 6.5 to full-on Edge Delivery Services, with multiple hybrid models in between. Each has tradeoffs across authoring experience, delivery model, backend extensibility, and real-world publishing speed.

Section 2: Generally Aligned Adobe Perspectives, I think

Universal Editor is no longer experimental. When properly instrumented, it's capable of in-context editing for everything from page content to experience fragments.

.model.json is still foundational for Sites and SPA use. Developers must define content models carefully to support authoring and preview. It's the OG omnichannel solution after .-1.json, which is a JCR dump, and I have heard folks use it as a source of render-able data to frontend.

Document-based authoring in EDS is fast, scalable, and predictable. It doesn’t support personalization or omnichannel out of the box, but it offers the lowest friction for publishing.

EDS in general shifting from disabling server side rendered content to server side compile time generated capabilities cached at edge side is what makes edge go fast

GraphQL and persisted queries represent the direction Adobe is pushing headless CMS. They allow structure, cacheability, and security.

Most developers underestimate the effort to fully enable UE. It’s not just a toggle. It's a dev workflow shift of having front end friends build dialogs and maybe even model definitions.

Section 3: Opinion Column, My Spicier Takes, Not Aligned with Anyone

Sites/Page with UE is a confusing middle-ground. You get in-context editing, but only if your .model.json and instrumentation are airtight. Or you can try and use .infinity.json as seen in https://ue-remote-app.adobe.net, which is also as confusing.

Headless CF + UE has strong omnichannel story but can be overkill if you're not integrating across multiple touchpoints. Or as referred by my previous blog, front end team is very strong or is tightly coupled with another vital system.

Classic AEM still has one of the best WYSIWYG experiences. But you carry all the weight of on-prem or container-based management. May not be as cool as UE, but way more functional and best in the industry.

Docs-based EDS authoring will scale faster than any other model. It's one of the few models where the authoring experience is so streamlined that content teams can scale independently of deep AEM development effort.

EDS will likely be coupled with other cloud solutions. One of the reasons why I personally focused on Cloud Engineering skills on Azure.

Part 3: How Things Could End Up

No single pattern wins. They all exist for a reason.

Sometimes it's political. Sometimes it's what the client asked for. Sometimes it's the shape of the wedding cake.

But knowing the tradeoffs and comparisons is vital to the first step of any implementation. Not every project has the luxury of time to evaluate seven options. But when you’ve seen the full map, you can steer better.

This matrix isn't a prescription. It’s a way to ask better questions.

